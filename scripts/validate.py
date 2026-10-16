#!/usr/bin/env python3
#=======================================================================================================================
# scripts/validate.py is part of DotBeer and is copyright the following authors 2026:
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
       • every reference points to an object of the right type (eg a recipe's style_id is the ID of a style)
     plus a few other cross-field consistency checks:
       • an addition schedule's `step` exists in the relevant mash / boil / fermentation procedure
       • a range's minimum is not greater than its maximum (where both use the same unit)
       • a brew log's ferment_date is not before its brew_date

Before any files are checked, the schema files themselves are checked: each must parse, and every "$ref" in them must
resolve.  (Otherwise a broken $ref is only reported if and when a file happens to exercise it.)

Files that are deliberately invalid (eg in examples/invalid/) must start with one or more comment lines of the form

    // EXPECT-INVALID: <text>

Such a file passes only if validation fails AND each <text> appears in at least one of the error messages.  This makes
sure a test file fails for the reason it is meant to, rather than some unrelated one.

Usage:
    scripts/validate.py                     # Validate everything under examples/
    scripts/validate.py foo.beer bar/       # Validate the given files and (recursively) directories

Exit status: 0 if all files give the expected result; 1 if any do not; 2 if the schema itself is broken.

Dependencies:
 - jsonschema (https://python-jsonschema.readthedocs.io/), version 4.18 or later, which brings in `referencing`
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import sys
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

#
# Every field that holds a cross-reference, mapped to the top-level section (of the DotBeer root object) in which the
# referred-to object must live.  If the schema gains a new "..._id" reference field, it needs adding here.  (We warn
# about any "..._id" field we don't recognise, so that we don't silently stop checking it.)
#
REFERENCE_FIELDS = {
    "style_id"        : "styles"       ,
    "equipment_id"    : "equipments"   ,
    "mash_id"         : "mashes"       ,
    "boil_id"         : "boils"        ,
    "fermentation_id" : "fermentations",
    "water_base_id"   : "waters"       ,
    "water_target_id" : "waters"       ,
    "fermentable_id"  : "fermentables" ,
    "hop_id"          : "hops"         ,
    "misc_id"         : "miscs"        ,
    "culture_id"      : "cultures"     ,
}

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

EXPECT_INVALID_RE = re.compile(r"^\s*//\s*EXPECT-INVALID:\s*(.+?)\s*$")


@dataclass
class Result:
    errors  : list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


#=======================================================================================================================
# Schema loading
#=======================================================================================================================
def load_schemas(schema_dir: Path) -> tuple[dict[str, Any], referencing.Registry]:
    """Returns the root schema and a registry containing all the schemas, keyed by their $id"""
    files = sorted(schema_dir.glob("*.beer.schema"))
    if not files:
        sys.exit(f"No *.beer.schema files found in {schema_dir}")

    registry: referencing.Registry = referencing.Registry()
    root = None
    for file in files:
        try:
            contents = JsoncParser.parse_file(str(file))
        except Exception as e:
            print(f"SCHEMA ERROR: cannot parse {file}: {e}")
            sys.exit(2)
        if "$id" not in contents:
            print(f"SCHEMA ERROR: {file} has no $id")
            sys.exit(2)
        registry = registry.with_resource(contents["$id"],
                                          referencing.Resource.from_contents(contents,
                                                                             default_specification=DRAFT202012))
        if file.name == "DotBeer.beer.schema":
            root = contents

    if root is None:
        sys.exit(f"DotBeer.beer.schema not found in {schema_dir}")
    return root, registry.crawl()


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
    problems = []
    for uri in sorted(registry):
        contents = registry.contents(uri)
        if not isinstance(contents, dict) or contents.get("$id") != uri:
            continue  # Subresource, not a schema file
        resolver = registry.resolver(base_uri=uri)
        file_name = uri.rsplit("/", 1)[-1]
        for pointer, ref in walk_refs(contents):
            try:
                resolver.lookup(ref)
            except referencing.exceptions.Unresolvable:
                problems.append(f"{file_name}{pointer or '/'}: $ref \"{ref}\" does not resolve")
    return problems


#=======================================================================================================================
# Pass 1: JSON Schema
#=======================================================================================================================
def describe_schema_error(error: jsonschema.ValidationError) -> str:
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
    return f"{path}: {error.message}"


def schema_errors(document: Any, validator: jsonschema.protocols.Validator) -> list[str]:
    errors = sorted(validator.iter_errors(document), key=lambda e: list(map(str, e.absolute_path)))
    return [describe_schema_error(e) for e in errors]


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


def check_references(root: dict, defined: dict[str, tuple[str, str, Any]], result: Result) -> None:
    for path, obj in walk(root, "/DotBeer"):
        if not isinstance(obj, dict):
            continue
        for key, value in obj.items():
            if key in REFERENCE_FIELDS:
                expected_section = REFERENCE_FIELDS[key]
                if not isinstance(value, str):
                    continue  # Schema validation will already have complained
                if value not in defined:
                    result.errors.append(f"{path}/{key}: local ID \"{value}\" is not defined anywhere in this file "
                                         f"(expected an item in \"{expected_section}\")")
                    continue
                actual_section, target_path, target = defined[value]
                if actual_section != expected_section:
                    result.errors.append(f"{path}/{key}: local ID \"{value}\" refers to {label(target, target_path)}, "
                                         f"which is in \"{actual_section}\", but {key} must refer to an item in "
                                         f"\"{expected_section}\"")
            elif key.endswith("_id") and key not in NON_REFERENCE_ID_FIELDS:
                result.warnings.append(f"{path}/{key}: field looks like a local ID reference, but validate.py does "
                                       f"not know what type it should refer to (update REFERENCE_FIELDS)")


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
                #
                # Per Boil.beer.schema, a boil with no steps is the same as a standard single-step boil
                #
                if stage == "add_to_boil":
                    num_steps = max(num_steps, 1)
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


def semantic_checks(document: Any, result: Result) -> None:
    root = document.get("DotBeer") if isinstance(document, dict) else None
    if not isinstance(root, dict):
        return  # Schema validation will already have complained
    defined = check_local_ids(root, result)
    check_references(root, defined, result)
    check_addition_steps(root, defined, result)
    check_ranges(root, result)
    check_brew_log_dates(root, result)


#=======================================================================================================================
# Driver
#=======================================================================================================================
def validate_file(path: Path, validator: jsonschema.protocols.Validator) -> Result:
    result = Result()
    try:
        document = JsoncParser.parse_file(str(path))
    except Exception as e:
        result.errors.append(f"cannot parse file: {e}")
        return result
    result.errors.extend(schema_errors(document, validator))
    semantic_checks(document, result)
    return result


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

    root_schema, registry = load_schemas(Path(args.schema_dir))

    ref_problems = check_schema_refs(registry)
    if ref_problems:
        print("SCHEMA ERROR: the schema files contain $refs that do not resolve:")
        for problem in ref_problems:
            print(f"    {problem}")
        return 2

    validator_class = jsonschema.validators.validator_for(root_schema)
    validator_class.check_schema(root_schema)
    validator = validator_class(root_schema, registry=registry, format_checker=validator_class.FORMAT_CHECKER)

    files = collect_files(args.paths)
    if not files:
        print("No .beer files found")
        return 1

    num_unexpected = 0
    for path in files:
        result = validate_file(path, validator)
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
