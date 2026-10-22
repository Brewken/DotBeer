#!/usr/bin/env python3
#=======================================================================================================================
# scripts/validate.py is part of dotBeer and is copyright the following authors 2026:
#   • Matt Young <mfsy@yahoo.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License (MPL), version 2.0.  If a copy of the MPL
# was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# DotBeer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Mozilla Public License for more details.
#=======================================================================================================================
"""
Validate dotBeer (.beer) files.

Each file is checked in two passes:

  1. Against the JSON Schema in the schema/ directory (JSON Schema 2020-12).

  2. Against the rules that JSON Schema cannot express (see the description of LocalId in DotBeer.beer.schema):
       • every local ID is unique within the file, across all object types
       • every referred-to local ID is defined in the same file
       • every reference points to an object of the right type (eg a recipe's style_id is the ID of a style, or a
         stock use's brew_log_id is the ID of a brew log in one of the recipes)
     plus a few other cross-field consistency checks:
       • an addition schedule's `step` exists in the relevant mash / boil / fermentation procedure
       • a range's minimum is not greater than its maximum (where both use the same unit)
       • a brew log's ferment_date is not before its brew_date
       • a stock purchase's date_received is not before its date_ordered, and no stock use is dated before the stock
         was received (or, if it hasn't been received, ordered)
       • a stock purchase's amounts (ordered, received and used) all measure the same kind of thing (eg all mass)
       • a stock purchase's uses don't add up to more than was received (or, if nothing was received, ordered)

When an error in a property that comes from an "allOf" (eg a bad `reason` in StockUseCommon) makes that part of the
schema fail, JSON Schema then also reports the part's other properties as "unevaluated".  These knock-on errors are
removed, so that only the real problem is reported.  (A property name that is not declared anywhere in the schema, eg a
typo, is still reported.)

Before any files are checked, the schema files themselves are checked: each must parse, and every "$ref" in them must
resolve.  (Otherwise a broken $ref is only reported if and when a file happens to exercise it.)

Files that are deliberately invalid (eg in examples/invalid/) must start with one or more comment lines of the form

    // EXPECT-INVALID: <text>

Such a file passes only if validation fails AND each <text> appears in at least one of the error messages.  This makes
sure a test file fails for the reason it is meant to, rather than some unrelated one.

Usage:
    scripts/validate.py                     # Validate everything under examples/
    scripts/validate.py foo.beer bar/       # Validate the given files and (recursively) directories

Files under examples/ must also have a "version" matching the version of the schema (ie the version in the schema files'
$ids), so that the examples get updated whenever the schema version changes.  For other files, a different version is
only a warning, since it is perfectly normal for a file to have been written with an older version of the schema.

Exit status: 0 if all files give the expected result; 1 if any do not; 2 if the schema itself is broken.

Dependencies:
 - jsonschema (https://python-jsonschema.readthedocs.io/), version 4.18 or later, which brings in `referencing`
"""

from __future__ import annotations

import argparse
import ast
import datetime
import os
import re
import sys
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jsonc_parser.parser import JsoncParser  # noqa: E402  (Same JSONC handling as generateDocs.py)

try:
    import jsonschema
    import referencing
    import referencing.exceptions
    from referencing.jsonschema import DRAFT202012
except ImportError:
    sys.exit("This script needs jsonschema 4.18 or later -- eg `pip install jsonschema`")

REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_DIR = REPO_ROOT / "examples"

#
# Fields ending in "_id" that are NOT local-ID cross-references
#
NON_REFERENCE_ID_FIELDS = {"local_id", "product_id"}

#
# For AdditionSchedule.stage, which recipe field gives the procedure, and which field of that procedure holds the steps
#
STAGE_PROCEDURES = {
    "add_to_mash"        : ("mash_id"        , "mash_steps"        ),
    "add_to_boil"        : ("boil_id"        , "boil_steps"        ),
    "add_to_fermentation": ("fermentation_id", "fermentation_steps"),
}

VERSION_RE = re.compile(r"^[0-9]+[.][0-9]+[.][0-9]+$")  # Same as VersionNumber in DotBeer.beer.schema

#
# For the stock checks, we need to know which units measure the same kind of thing (so we can spot, eg, a purchase
# received by mass but used by volume) and how to convert between them (so we can add up uses in different units).
# For each measure in Measurement.beer.schema, this gives the size of each unit in terms of a canonical one.  At start-up
# we check that the units here match the enums in the schema, so this can't silently get out of step with it.
#
# A few units have more than one definition in common use.  Here we take: bbl = US beer barrel = 31 US gallons (rather
# than the 31.5 US gallon barrel used for other liquids); ibbl = imperial beer barrel = 36 imperial gallons; and
# 1 icup = 10 ifloz (ie half an imperial pint).  For imperial spoons, we use the traditional British definitions: 1 itsp
# = 1 imperial fluid drachm = 1/8 ifloz, and 1 itbsp = 4 itsp = 1/2 ifloz.  (NB this differs from the US, where
# 1 tbsp = 3 tsp.)  These should match whatever Brewtarget/Brewken uses.  (The exact factors only matter here when uses
# in different units add up to almost exactly the amount purchased.)
#
UNIT_CONVERSIONS: dict[str, dict[str, float]] = {
    "Mass": {  # In grams
        "mg" : 0.001,
        "g"  : 1.0,
        "kg" : 1000.0,
        "lb" : 453.59237,
        "oz" : 28.349523125,
    },
    "Volume": {  # In milliliters
        "ml"   : 1.0,
        "l"    : 1000.0,
        "tsp"  : 4.92892159375,
        "tbsp" : 14.78676478125,
        "floz" : 29.5735295625,
        "cup"  : 236.5882365,
        "pt"   : 473.176473,
        "qt"   : 946.352946,
        "gal"  : 3785.411784,
        "bbl"  : 117347.765304,  # US beer barrel = 31 US gallons
        "itsp" : 3.5516328125,
        "itbsp": 14.20653125,
        "ifloz": 28.4130625,
        "icup" : 284.130625,
        "ipt"  : 568.26125,
        "iqt"  : 1136.5225,
        "igal" : 4546.09,
        "ibbl" : 163659.24,  # Imperial beer barrel = 36 imperial gallons
    },
    "Count": {
        "count": 1.0,
    },
}
UNIT_TO_MEASURE = {unit: measure for measure, units in UNIT_CONVERSIONS.items() for unit in units}

#
# Allow for floating-point rounding when adding up amounts in different units
#
STOCK_TOLERANCE = 1e-9

#
# Matches each quoted property name in a jsonschema "Unevaluated properties are not allowed (...)" message
#
QUOTED_NAME_RE = re.compile(r"""'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)\"""")

EXPECT_INVALID_RE = re.compile(r"^\s*//\s*EXPECT-INVALID:\s*(.+?)\s*$")


@dataclass
class Result:
    errors  : list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    # Set if the file's "version" differs from the schema version.  Kept separate from `errors` because it is handled
    # differently depending on whether the file is one of our examples (see main()).
    version_mismatch: str | None = None


#=======================================================================================================================
# Schema loading
#=======================================================================================================================
def load_schemas(schema_dir: Path) -> tuple[dict[str, Any], referencing.Registry, str]:
    """
    Returns the root schema, a registry containing all the schemas (keyed by their $id), and the schema version (taken
    from the $ids, which all have the form https://dotbeer.org/schema/<version>/<file name>)
    """
    files = sorted(schema_dir.glob("*.beer.schema"))
    if not files:
        sys.exit(f"No *.beer.schema files found in {schema_dir}")

    registry: referencing.Registry = referencing.Registry()
    root = None
    id_to_file: dict[str, Path] = {}
    version_to_files: dict[str, list[str]] = {}
    for file in files:
        try:
            contents = JsoncParser.parse_file(str(file))
        except Exception as e:
            print(f"SCHEMA ERROR: cannot parse {file}: {e}")
            sys.exit(2)
        if not isinstance(contents, dict) or "$id" not in contents:
            print(f"SCHEMA ERROR: {file} has no $id")
            sys.exit(2)
        #
        # If two files declare the same $id, the later one silently replaces the earlier one in the registry, and every
        # $ref into the earlier one then fails.  (Easy to do when copying an existing schema file to start a new one.)
        #
        if contents["$id"] in id_to_file:
            print(f"SCHEMA ERROR: {file.name} and {id_to_file[contents['$id']].name} both have "
                  f"$id \"{contents['$id']}\"")
            sys.exit(2)
        id_to_file[contents["$id"]] = file
        #
        # The $id should end with the file name, otherwise relative $refs such as "Hop.beer.schema#/..." will not find
        # the file.
        #
        if contents["$id"].rsplit("/", 1)[-1] != file.name:
            print(f"SCHEMA ERROR: {file.name} has $id \"{contents['$id']}\", which does not end with the file name")
            sys.exit(2)
        #
        # The "directory" above the file name is the schema version, and it needs to be the same for all the files.
        # (Easy to get wrong when bumping the version, as it has to be changed in every file.)
        #
        id_parts = urllib.parse.urlparse(contents["$id"]).path.rstrip("/").split("/")
        version = id_parts[-2] if len(id_parts) >= 2 else ""
        if not VERSION_RE.match(version):
            print(f"SCHEMA ERROR: {file.name} has $id \"{contents['$id']}\", which does not contain a version number "
                  f"before the file name")
            sys.exit(2)
        version_to_files.setdefault(version, []).append(file.name)
        registry = registry.with_resource(contents["$id"],
                                          referencing.Resource.from_contents(contents,
                                                                             default_specification=DRAFT202012))
        if file.name == "DotBeer.beer.schema":
            root = contents

    if root is None:
        sys.exit(f"DotBeer.beer.schema not found in {schema_dir}")
    if len(version_to_files) > 1:
        print("SCHEMA ERROR: the schema files do not all have the same version in their $id:")
        for version, names in sorted(version_to_files.items()):
            print(f"    {version}: {', '.join(names)}")
        sys.exit(2)
    return root, registry.crawl(), next(iter(version_to_files))


def walk_refs(node: Any, pointer: str = "") -> Iterator[tuple[str, str]]:
    """Yields (JSON pointer, $ref value) for every $ref in a schema"""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str):
                yield pointer, value
            else:
                yield from walk_refs(value, f"{pointer}/{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_refs(value, f"{pointer}/{index}")


def check_schema_refs(registry: referencing.Registry) -> list[str]:
    """Returns a list of problems with $refs that do not resolve"""
    schema_uris = sorted(uri for uri in registry
                         if isinstance(registry.contents(uri), dict) and registry.contents(uri).get("$id") == uri)
    problems = []
    missing_documents: dict[str, list[str]] = {}
    for uri in schema_uris:
        contents = registry.contents(uri)
        resolver = registry.resolver(base_uri=uri)
        file_name = uri.rsplit("/", 1)[-1]
        for pointer, ref in walk_refs(contents):
            where = f"{file_name}{pointer or '/'}"
            try:
                resolver.lookup(ref)
            except referencing.exceptions.Unresolvable:
                #
                # Distinguish "the referred-to schema file isn't loaded at all" (where we report once, rather than once
                # per $ref) from "the file is loaded but has no such definition".
                #
                target = urllib.parse.urljoin(uri, ref).split("#", 1)[0]
                if target not in schema_uris:
                    missing_documents.setdefault(target, []).append(where)
                else:
                    problems.append(f"{where}: $ref \"{ref}\" does not resolve")
    for target, wheres in sorted(missing_documents.items()):
        problems.insert(0, f"no schema file has $id \"{target}\", but {len(wheres)} $ref(s) refer to it "
                           f"(eg {wheres[0]}).  Loaded $ids are:\n" +
                           "\n".join(f"        {u}" for u in schema_uris))
    return problems


def walk_refers_to(node: Any, pointer: str = "") -> Iterator[tuple[str, str, Any]]:
    """
    Yields (JSON pointer, property name, "x-refers-to" value) for every property schema that has an "x-refers-to"
    annotation.  (This is our own keyword: it says that the property holds a local ID, and gives, as a JSON Pointer into
    the dotBeer file, the array in which the referred-to object must be.  Eg "x-refers-to": "/DotBeer/hops".)

    A "*" token matches any index of an array, for objects that are nested inside other objects.  Eg
    "x-refers-to": "/DotBeer/recipes/*/brew_logs" means the referred-to object must be a brew log of some recipe.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{pointer}/{key}"
            if pointer.endswith("/properties") and isinstance(value, dict) and "x-refers-to" in value:
                yield child, key, value["x-refers-to"]
            yield from walk_refers_to(value, child)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_refers_to(value, f"{pointer}/{index}")


def split_json_pointer(pointer: str) -> list[str]:
    """Splits a JSON Pointer (RFC 6901) into its (unescaped) reference tokens"""
    return [token.replace("~1", "/").replace("~0", "~") for token in pointer.split("/")[1:]]


def deref(node: Any, resolver: referencing.Resolver) -> tuple[Any, referencing.Resolver]:
    """
    Follows "$ref"s until we get to a schema that is not just a reference.  Returns that schema and the resolver to use
    for any relative "$ref"s inside it (which may be in a different schema file from the one we started in).
    """
    seen = set()
    while isinstance(node, dict) and isinstance(node.get("$ref"), str):
        if id(node) in seen:
            break  # Circular $ref -- shouldn't happen in our schema, but don't loop forever if it does
        seen.add(id(node))
        resolved = resolver.lookup(node["$ref"])
        node, resolver = resolved.contents, resolved.resolver
    return node, resolver


def schema_for_pointer(registry: referencing.Registry, root_schema: dict[str, Any], pointer: str) -> Any:
    """
    Returns the schema that applies, in a dotBeer file, at the place given by a JSON Pointer such as "/DotBeer/hops" or
    "/DotBeer/recipes/*/brew_logs", or None if there is no such place.  A "*" token means "any item of this array".

    We follow "$ref"s (so that we can get from the root schema into, eg, Recipe.beer.schema), "properties" and "items".
    We don't look inside "allOf" etc, as that is not needed for any of the places local IDs are currently defined.
    """
    node: Any = root_schema
    resolver = registry.resolver(base_uri=root_schema["$id"])
    for token in split_json_pointer(pointer):
        node, resolver = deref(node, resolver)
        if not isinstance(node, dict):
            return None
        if token == "*":
            if node.get("type") != "array":
                return None
            node = node.get("items")
        else:
            node = node.get("properties", {}).get(token)
        if node is None:
            return None
    node, _ = deref(node, resolver)
    return node


def pointer_matches(pattern: str, pointer: str) -> bool:
    """
    True if a JSON Pointer to an array in a dotBeer file (eg "/DotBeer/recipes/2/brew_logs") matches an "x-refers-to"
    target (eg "/DotBeer/recipes/*/brew_logs"), where "*" matches any array index.
    """
    pattern_tokens, pointer_tokens = split_json_pointer(pattern), split_json_pointer(pointer)
    return len(pattern_tokens) == len(pointer_tokens) and all(
        p == a or (p == "*" and a.isdigit()) for p, a in zip(pattern_tokens, pointer_tokens)
    )


def load_reference_fields(registry: referencing.Registry,
                          root_schema: dict[str, Any]) -> tuple[dict[str, str], list[str]]:
    """
    Returns a map from the name of each property that holds a local-ID cross-reference to the JSON Pointer of the array
    (in a dotBeer file) where the referred-to object must be, plus a list of any problems with the "x-refers-to"
    annotations.

    NB: We key on property name alone, so the same property name must refer to the same place wherever it is used.
    """
    schema_uris = sorted(uri for uri in registry
                         if isinstance(registry.contents(uri), dict) and registry.contents(uri).get("$id") == uri)
    fields: dict[str, tuple[str, str]] = {}  # property name -> (target, where defined)
    problems = []
    for uri in schema_uris:
        file_name = uri.rsplit("/", 1)[-1]
        for pointer, name, target in walk_refers_to(registry.contents(uri)):
            where = f"{file_name}{pointer}"
            if not isinstance(target, str) or not target.startswith("/"):
                problems.append(f"{where}: x-refers-to must be a JSON Pointer string, eg \"/DotBeer/hops\"")
                continue
            #
            # Check the target exists in the schema, by following it down from the root schema.  (This needs to
            # follow $refs because targets such as "/DotBeer/recipes/*/brew_logs" are inside other schema files.)
            #
            try:
                node = schema_for_pointer(registry, root_schema, target)
            except referencing.exceptions.Unresolvable:
                node = None  # check_schema_refs() will normally have caught this already
            if not isinstance(node, dict) or node.get("type") != "array":
                problems.append(f"{where}: x-refers-to \"{target}\" is not an array in the schema")
                continue
            if name in fields and fields[name][0] != target:
                problems.append(f"{where}: x-refers-to \"{target}\" conflicts with \"{fields[name][0]}\" for the "
                                f"same property name at {fields[name][1]}")
                continue
            fields.setdefault(name, (target, where))
    return {name: target for name, (target, _) in fields.items()}, problems


def walk_formats(node: Any, pointer: str = "") -> Iterator[tuple[str, str]]:
    """Yields (JSON pointer, format value) for every "format" keyword in a schema"""
    if isinstance(node, dict):
        for key, value in node.items():
            #
            # Inside "properties", keys are property names rather than keywords, so a property called "format" is not a
            # format keyword
            #
            if key == "format" and isinstance(value, str) and not pointer.endswith("/properties"):
                yield pointer, value
            else:
                yield from walk_formats(value, f"{pointer}/{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_formats(value, f"{pointer}/{index}")


def check_format_support(registry: referencing.Registry, format_checker: jsonschema.FormatChecker) -> list[str]:
    """
    Returns a warning for each "format" used in the schema that the format checker cannot actually check.

    Several of jsonschema's format checkers depend on optional packages (eg "date-time" needs rfc3339-validator).  If
    the package is not installed, the format is silently treated as valid, so, eg, "2026-02-30T08:00:00Z" would be
    accepted.  (The "pattern" on such fields still catches most, but not all, mistakes.)
    """
    schema_uris = sorted(uri for uri in registry
                         if isinstance(registry.contents(uri), dict) and registry.contents(uri).get("$id") == uri)
    used: dict[str, str] = {}
    for uri in schema_uris:
        file_name = uri.rsplit("/", 1)[-1]
        for pointer, format_name in walk_formats(registry.contents(uri)):
            used.setdefault(format_name, f"{file_name}{pointer or '/'}")
    return [f"format \"{format_name}\" (used at eg {where}) is not being checked -- for full checking, "
            f"install jsonschema with the format extras, eg `pip install \"jsonschema[format-nongpl]\"`"
            for format_name, where in sorted(used.items()) if format_name not in format_checker.checkers]


def check_unit_tables(registry: referencing.Registry) -> list[str]:
    """
    Returns a list of problems where UNIT_CONVERSIONS (above) does not match the units in Measurement.beer.schema
    """
    measurement = next((registry.contents(uri) for uri in registry
                        if uri.endswith("/Measurement.beer.schema")), None)
    if not isinstance(measurement, dict):
        return ["cannot find Measurement.beer.schema"]
    problems = []
    for measure, conversions in UNIT_CONVERSIONS.items():
        try:
            schema_units = set(measurement["$defs"][measure]["properties"]["unit"]["enum"])
        except (KeyError, TypeError):
            problems.append(f"Measurement.beer.schema has no unit enum for {measure}")
            continue
        if schema_units != set(conversions):
            missing = sorted(schema_units - set(conversions))
            extra   = sorted(set(conversions) - schema_units)
            problems.append(f"units for {measure} in validate.py do not match Measurement.beer.schema "
                            f"(missing from validate.py: {missing or 'none'}; not in schema: {extra or 'none'})")
    return problems


def declared_property_names(registry: referencing.Registry) -> set[str]:
    """Returns the name of every property declared (in a "properties" keyword) anywhere in the schema"""
    names: set[str] = set()

    def visit(node: Any) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "properties" and isinstance(value, dict):
                    names.update(value.keys())
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)

    for uri in registry:
        visit(registry.contents(uri))
    return names


#=======================================================================================================================
# Pass 1: JSON Schema
#=======================================================================================================================
def describe_schema_error(error: jsonschema.ValidationError, message: str | None = None) -> str:
    #
    # For oneOf/anyOf failures, the top-level message just dumps the whole instance, which is not very helpful.  Where
    # there is a more specific underlying error, report that instead.
    #
    if error.context:
        best = jsonschema.exceptions.best_match(error.context)
        if best is not None:
            error = best
    # Use JSON Pointer notation, for consistency with the messages from the other checks
    path = "".join(f"/{p}" for p in error.absolute_path) or "(root)"
    return f"{path}: {message if message is not None else error.message}"


def unevaluated_names(error: jsonschema.ValidationError) -> list[str]:
    """Returns the property names listed in an "Unevaluated properties are not allowed (...)" error"""
    names = []
    for match in QUOTED_NAME_RE.finditer(error.message):
        try:
            names.append(ast.literal_eval(match.group(0)))
        except (ValueError, SyntaxError):
            names.append(match.group(1) if match.group(1) is not None else match.group(2))
    return names


def schema_errors(document: Any, validator: jsonschema.protocols.Validator, declared_names: set[str]) -> list[str]:
    errors = sorted(validator.iter_errors(document), key=lambda e: list(map(str, e.absolute_path)))
    #
    # If part of an "allOf" fails (eg because StockUseCommon's `reason` has a bad value), JSON Schema treats all that
    # part's properties as not evaluated, so `"unevaluatedProperties": false` then reports them as unexpected, even
    # though they are perfectly valid.  We drop such knock-on errors, ie unevaluated properties that are declared
    # somewhere in the schema, in an object where (or inside which) there is another error.  We keep any property name
    # that is not declared anywhere (eg a typo), and we keep everything if there is no other error in the object (so
    # that, eg, a fermentable_id in a hop stock purchase is still reported).
    #
    other_error_paths = [tuple(e.absolute_path) for e in errors if e.validator != "unevaluatedProperties"]
    descriptions = []
    for error in errors:
        if error.validator == "unevaluatedProperties":
            path = tuple(error.absolute_path)
            if any(other[:len(path)] == path for other in other_error_paths):
                names = unevaluated_names(error)
                remaining = [name for name in names if name not in declared_names]
                if not remaining:
                    continue
                if len(remaining) < len(names):
                    descriptions.append(describe_schema_error(
                        error,
                        f"Unevaluated properties are not allowed ({', '.join(map(repr, remaining))} "
                        f"{'was' if len(remaining) == 1 else 'were'} unexpected)"
                    ))
                    continue
        descriptions.append(describe_schema_error(error))
    return descriptions


#=======================================================================================================================
# Pass 2: Things JSON Schema can't check
#=======================================================================================================================
def label(obj: Any, path: str) -> str:
    """Path plus, where available, the object's name -- to make messages easier to relate to the file"""
    if isinstance(obj, dict) and isinstance(obj.get("name"), str):
        return f"{path} (\"{obj['name']}\")"
    return path


def walk(node: Any, path: str = "") -> Iterator[tuple[str, Any]]:
    """Yields (JSON pointer, node) for every object in the document"""
    yield path, node
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk(value, f"{path}/{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk(value, f"{path}/{index}")


def check_local_ids(root: dict, result: Result) -> dict[str, tuple[str, str, Any]]:
    """
    Checks local IDs are unique across the whole file, and returns a map from local ID to (section, path, object)
    """
    defined: dict[str, tuple[str, str, Any]] = {}
    for section, items in root.items():
        if not isinstance(items, list):
            continue
        for path, obj in walk(items, f"/DotBeer/{section}"):
            if not isinstance(obj, dict) or not isinstance(obj.get("local_id"), str):
                continue
            local_id = obj["local_id"]
            if local_id in defined:
                _, first_path, first_obj = defined[local_id]
                result.errors.append(f"{label(obj, path)}: duplicate local ID \"{local_id}\" "
                                     f"(already used by {label(first_obj, first_path)})")
            else:
                defined[local_id] = (section, path, obj)
    return defined


def check_references(root: dict, defined: dict[str, tuple[str, str, Any]], reference_fields: dict[str, str],
                     result: Result) -> None:
    for path, obj in walk(root, "/DotBeer"):
        if not isinstance(obj, dict):
            continue
        for key, value in obj.items():
            if key in reference_fields:
                expected = reference_fields[key]
                if not isinstance(value, str):
                    continue  # Schema validation will already have complained
                if value not in defined:
                    result.errors.append(f"{path}/{key}: local ID \"{value}\" is not defined anywhere in this file "
                                         f"(expected an item in {expected})")
                    continue
                _, target_path, target = defined[value]
                actual = target_path.rsplit("/", 1)[0]
                if not pointer_matches(expected, actual):
                    result.errors.append(f"{path}/{key}: local ID \"{value}\" refers to {label(target, target_path)}, "
                                         f"which is in {actual}, but {key} must refer to an item in {expected}")
            elif key.endswith("_id") and key not in NON_REFERENCE_ID_FIELDS:
                result.warnings.append(f"{path}/{key}: field looks like a local ID reference, but its schema has no "
                                       f"x-refers-to annotation, so validate.py cannot check it")


def check_addition_steps(root: dict, defined: dict[str, tuple[str, str, Any]], result: Result) -> None:
    for recipe_index, recipe in enumerate(root.get("recipes", [])):
        if not isinstance(recipe, dict):
            continue
        recipe_path = f"/DotBeer/recipes/{recipe_index}"
        ingredients = recipe.get("ingredients", {})
        if not isinstance(ingredients, dict):
            continue
        for list_name, additions in ingredients.items():
            if not isinstance(additions, list):
                continue
            for index, addition in enumerate(additions):
                schedule = addition.get("schedule") if isinstance(addition, dict) else None
                if not isinstance(schedule, dict) or "step" not in schedule:
                    continue
                stage = schedule.get("stage")
                if stage not in STAGE_PROCEDURES:
                    continue  # Eg add_to_package -- no steps to check against
                where = f"{recipe_path}/ingredients/{list_name}/{index}/schedule/step"
                id_field, steps_field = STAGE_PROCEDURES[stage]
                procedure_id = recipe.get(id_field)
                if procedure_id is None:
                    result.errors.append(f"{where}: schedule is for step {schedule['step']} of {stage}, but recipe "
                                         f"\"{recipe.get('name')}\" has no {id_field}")
                    continue
                if procedure_id not in defined:
                    continue  # Already reported as a dangling reference
                procedure = defined[procedure_id][2]
                num_steps = len(procedure.get(steps_field, []))
                if isinstance(schedule["step"], int) and schedule["step"] > num_steps:
                    result.errors.append(f"{where}: schedule is for step {schedule['step']} of {stage}, but "
                                         f"\"{procedure.get('name')}\" only has {num_steps} step(s)")


def check_ranges(root: dict, result: Result) -> None:
    for path, obj in walk(root, "/DotBeer"):
        if not isinstance(obj, dict) or set(obj.keys()) != {"minimum", "maximum"}:
            continue
        low, high = obj["minimum"], obj["maximum"]
        if not (isinstance(low, dict) and isinstance(high, dict)):
            continue
        if low.get("unit") != high.get("unit"):
            continue  # Would need unit conversion -- not worth it here
        try:
            if low["value"] > high["value"]:
                result.errors.append(f"{path}: minimum ({low['value']} {low['unit']}) is greater than maximum "
                                     f"({high['value']} {high['unit']})")
        except (KeyError, TypeError):
            pass  # Schema validation will already have complained


def check_brew_log_dates(root: dict, result: Result) -> None:
    for recipe_index, recipe in enumerate(root.get("recipes", [])):
        if not isinstance(recipe, dict):
            continue
        for log_index, log in enumerate(recipe.get("brew_logs", [])):
            if not isinstance(log, dict) or "brew_date" not in log or "ferment_date" not in log:
                continue
            try:
                brew_date    = datetime.date.fromisoformat(log["brew_date"])
                ferment_date = datetime.date.fromisoformat(log["ferment_date"])
            except (TypeError, ValueError):
                continue  # Schema validation will already have complained
            if ferment_date < brew_date:
                result.errors.append(f"/DotBeer/recipes/{recipe_index}/brew_logs/{log_index}: ferment_date "
                                     f"{ferment_date} is before brew_date {brew_date}")


def parse_date(value: Any) -> datetime.date | None:
    """Returns the date, or None if it is missing or invalid (in which case schema validation will have complained)"""
    try:
        return datetime.date.fromisoformat(value) if isinstance(value, str) else None
    except ValueError:
        return None


def amount_in_canonical_units(amount: Any) -> tuple[str, float] | None:
    """
    For an amount such as {"unit": "kg", "value": 1.5}, returns the measure and the value in the canonical unit for that
    measure (eg ("Mass", 1500.0)), or None if the amount is missing or invalid (which schema validation will report)
    """
    if not isinstance(amount, dict):
        return None
    unit, value = amount.get("unit"), amount.get("value")
    if unit not in UNIT_TO_MEASURE or isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    measure = UNIT_TO_MEASURE[unit]
    return measure, value * UNIT_CONVERSIONS[measure][unit]


def describe_amount(amount: dict) -> str:
    return f"{amount['value']:g} {amount['unit']}"


def check_stock_purchases(root: dict, result: Result) -> None:
    for section, purchases in root.items():
        if not section.endswith("_stock_purchases") or not isinstance(purchases, list):
            continue
        for index, purchase in enumerate(purchases):
            if not isinstance(purchase, dict):
                continue
            path = f"/DotBeer/{section}/{index}"
            stock_uses = purchase.get("stock_uses", [])
            if not isinstance(stock_uses, list):
                stock_uses = []  # Schema validation will already have complained

            #
            # Dates
            #
            date_ordered  = parse_date(purchase.get("date_ordered"))
            date_received = parse_date(purchase.get("date_received"))
            if date_ordered and date_received and date_received < date_ordered:
                result.errors.append(f"{label(purchase, path)}: date_received {date_received} is before date_ordered "
                                     f"{date_ordered}")
            #
            # If the stock hasn't been received (yet), we can at least check it wasn't used before it was ordered
            #
            earliest, earliest_field = (date_received, "date_received") if date_received else \
                                       (date_ordered , "date_ordered" )
            if earliest:
                for use_index, use in enumerate(stock_uses):
                    use_date = parse_date(use.get("date")) if isinstance(use, dict) else None
                    if use_date and use_date < earliest:
                        result.errors.append(f"{path}/stock_uses/{use_index}: date {use_date} is before the "
                                             f"purchase's {earliest_field} {earliest}")

            #
            # Amounts: first check they all measure the same kind of thing, then that uses don't exceed what we have
            #
            amounts: list[tuple[str, dict, str, float]] = []  # (where, amount, measure, value in canonical units)
            for field_name in ("amount_ordered", "amount_received"):
                converted = amount_in_canonical_units(purchase.get(field_name))
                if converted:
                    amounts.append((f"{path}/{field_name}", purchase[field_name], *converted))
            for use_index, use in enumerate(stock_uses):
                converted = amount_in_canonical_units(use.get("amount_used")) if isinstance(use, dict) else None
                if converted:
                    amounts.append((f"{path}/stock_uses/{use_index}/amount_used", use["amount_used"], *converted))
            measures = {measure for _, _, measure, _ in amounts}
            if len(measures) > 1:
                result.errors.append(
                    f"{label(purchase, path)}: amounts must all be the same kind of measure, but there is a mix of "
                    f"{', '.join(sorted(m.lower() for m in measures))} (" +
                    "; ".join(f"{where.removeprefix(path + '/')} is {describe_amount(amount)}"
                              for where, amount, _, _ in amounts) + ")"
                )
                continue  # Can't meaningfully add up the uses

            available_field = "amount_received" if "amount_received" in purchase else "amount_ordered"
            available = amount_in_canonical_units(purchase.get(available_field))
            used = [(amount, value) for where, amount, _, value in amounts if "/stock_uses/" in where]
            if available and used:
                total_used = sum(value for _, value in used)
                if total_used > available[1] * (1 + STOCK_TOLERANCE):
                    unit = purchase[available_field]["unit"]
                    in_unit = total_used / UNIT_CONVERSIONS[available[0]][unit]
                    result.errors.append(
                        f"{label(purchase, path)}: stock uses total {in_unit:.6g} {unit}, which is more than the "
                        f"{describe_amount(purchase[available_field])} of {available_field}"
                    )


def semantic_checks(document: Any, reference_fields: dict[str, str], result: Result) -> None:
    root = document.get("DotBeer") if isinstance(document, dict) else None
    if not isinstance(root, dict):
        return  # Schema validation will already have complained
    defined = check_local_ids(root, result)
    check_references(root, defined, reference_fields, result)
    check_addition_steps(root, defined, result)
    check_ranges(root, result)
    check_brew_log_dates(root, result)
    check_stock_purchases(root, result)


#=======================================================================================================================
# Driver
#=======================================================================================================================
def validate_file(path: Path, validator: jsonschema.protocols.Validator, schema_version: str,
                  reference_fields: dict[str, str], declared_names: set[str]) -> Result:
    result = Result()
    try:
        document = JsoncParser.parse_file(str(path))
    except Exception as e:
        result.errors.append(f"cannot parse file: {e}")
        return result
    result.errors.extend(schema_errors(document, validator, declared_names))
    semantic_checks(document, reference_fields, result)
    root = document.get("DotBeer") if isinstance(document, dict) else None
    file_version = root.get("version") if isinstance(root, dict) else None
    if isinstance(file_version, str) and file_version != schema_version:  # If not a string, schema already complained
        result.version_mismatch = (f"/DotBeer/version: file is version {file_version}, but the schema is version "
                                   f"{schema_version}")
    return result


def is_example(path: Path) -> bool:
    return path.resolve().is_relative_to(EXAMPLES_DIR.resolve())


def expected_failures(path: Path) -> list[str]:
    """Reads the EXPECT-INVALID lines from the comment block at the top of the file"""
    expectations = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            if not line.lstrip().startswith("//"):
                break
            match = EXPECT_INVALID_RE.match(line)
            if match:
                expectations.append(match.group(1))
    return expectations


def collect_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for p in map(Path, paths):
        if p.is_dir():
            files.extend(sorted(p.rglob("*.beer")))
        elif p.is_file():
            files.append(p)
        else:
            sys.exit(f"No such file or directory: {p}")
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate dotBeer files against the schema and local-ID rules")
    parser.add_argument("paths", nargs="*", default=[str(REPO_ROOT / "examples")],
                        help=".beer files, or directories to search recursively (default: examples/)")
    parser.add_argument("--schema-dir", default=str(REPO_ROOT / "schema"),
                        help="directory containing the *.beer.schema files (default: schema/)")
    parser.add_argument("-q", "--quiet", action="store_true", help="only report files with unexpected results")
    args = parser.parse_args()

    root_schema, registry, schema_version = load_schemas(Path(args.schema_dir))

    ref_problems = check_schema_refs(registry)
    if ref_problems:
        print("SCHEMA ERROR: the schema files contain $refs that do not resolve:")
        for problem in ref_problems:
            print(f"    {problem}")
        return 2

    reference_fields, refers_to_problems = load_reference_fields(registry, root_schema)
    if refers_to_problems:
        print("SCHEMA ERROR: problems with x-refers-to annotations:")
        for problem in refers_to_problems:
            print(f"    {problem}")
        return 2

    unit_problems = check_unit_tables(registry)
    if unit_problems:
        print("SCHEMA ERROR: validate.py's unit tables are out of date:")
        for problem in unit_problems:
            print(f"    {problem}")
        return 2
    declared_names = declared_property_names(registry)

    validator_class = jsonschema.validators.validator_for(root_schema)
    validator_class.check_schema(root_schema)
    validator = validator_class(root_schema, registry=registry, format_checker=validator_class.FORMAT_CHECKER)

    for warning in check_format_support(registry, validator_class.FORMAT_CHECKER):
        print(f"WARNING: {warning}")

    files = collect_files(args.paths)
    if not files:
        print("No .beer files found")
        return 1

    num_unexpected = 0
    for path in files:
        result = validate_file(path, validator, schema_version, reference_fields, declared_names)
        expectations = expected_failures(path)
        try:
            shown = path.resolve().relative_to(Path.cwd())
        except ValueError:
            shown = path

        if not expectations:
            ok = not result.errors
            status = "PASS" if ok else "FAIL"
        elif not result.errors:
            ok, status = False, "FAIL (expected to be invalid, but passed validation)"
        else:
            missing = [x for x in expectations if not any(x in e for e in result.errors)]
            ok = not missing
            status = ("PASS (invalid, as expected)" if ok else
                      "FAIL (invalid, but not for the expected reason: " + "; ".join(f'"{m}"' for m in missing) + ")")

        #
        # A version mismatch fails an example even if the example is meant to be invalid (otherwise the "expected"
        # errors would hide it).  For any other file, it's just a warning.
        #
        if result.version_mismatch:
            if is_example(path):
                ok = False
                status = "FAIL (example is not at the current schema version)"
                result.errors.insert(0, result.version_mismatch)
            else:
                result.warnings.insert(0, result.version_mismatch)

        if not ok:
            num_unexpected += 1
        if ok and args.quiet:
            continue
        print(f"{status}: {shown}")
        #
        # For files that are meant to be invalid, only show the errors if something went wrong
        #
        if not ok or not expectations:
            for error in result.errors:
                print(f"    error: {error}")
        for warning in result.warnings:
            print(f"    warning: {warning}")

    print(f"\n{len(files)} file(s) checked, {num_unexpected} with unexpected results")
    return 1 if num_unexpected else 0


if __name__ == "__main__":
    sys.exit(main())
