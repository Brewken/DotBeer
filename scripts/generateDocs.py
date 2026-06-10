#!/usr/bin/env python3
#======================================================================================================================
# scripts/generateDocs.py is part of DotBeer and is copyright the following authors 2026:
#   • Matt Young <mfsy@yahoo.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License (MPL), version 2.0.  If a copy of the MPL
# was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# DotBeer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Mozilla Public License for more details.
#======================================================================================================================

#
# This script generates Markdown documentation from our .beer.schema files.  The generated Markdown files are checked in
# to GitHub to make them easily available to those interested in the project.
#
# For the moment, at least, we assume it is not necessary to directly generate documetation in other formats, because,
# eg, HTML documentation can be automatically generated from Markdown.  This, eg, is done by Jekyll in GitHub pages.
# NOTE that, as you might expect, GitHub pages has some level of caching.  So, when you publish an update to the
# documentation, the changes show up straight away in https://github.com/Brewken/DotBeer/tree/main/docs, but only after
# a delay of a few minutes in http://www.dotbeer.org/docs/DotBeer.html and related pages.  (This is one reason we have
# a generation timestamp at the bottom of each page!)
#

#
# Whilst there are several generic tools for creating documentation from JSON Schema files (eg jsonschema-markdown from
# https://github.com/elisiariocouto/jsonschema-markdown) I didn't find one in Python that elegantly handles a schema
# spread across multiple files.  (By "elegantly", I mean generating a separate Markdown file for each schema file and
# ensuring all the cross-references between the files are hyperlinks in the Markdown.)
#
# Since our schema is not hugely complicated, we therefore roll our own documentation generator, using customised
# versions of the following tools:
#
#   * jsonc-parser from https://github.com/NickolaiBeloguzov/jsonc-parser under MIT license
#     Out of the box, this does not accept files unless they have a ".json" or ".jsonc" extension.  We make a small
#     tweak to eliminate this constraint.  Hopefully the base project will be extended to allow any file extension (see
#     https://github.com/NickolaiBeloguzov/jsonc-parser/issues/9.)  Once this is done, we no longer need our customised
#     version.
#
#   * jsonschema-markdown from https://github.com/elisiariocouto/jsonschema-markdown under MIT license
#     This does a fair bit of what we want, but we tweak it heavily to our needs.  Our tweaks are a bit on the
#     hard-coded side, so unfortunately they are not easy/useful to contribute back to the main project.
#

import argparse
import glob
import inspect
import os

from datetime import datetime
from datetime import timezone

from jsonc_parser.parser import JsoncParser

import markdownGenerator

#
# Given an input list (inputList) and a preferred order (preferredOrder), returns a "sorted" version of inputList where:
#    - Any elements in inputList that are also in preferredOrder come first and in the same order as preferredOrder
#    - Remaining elements are ordered alphabetically
#
def sortWithPreference(inputList, preferredOrder):
   #
   # Calling enumerate() gives us a list of (index, element) pairs for all elements in preferredOrder
   # We then loop through that to construct a dictionary element->index for all elements in preferredOrder
   #
   preferredOrderIndexLookup = {element: index for index, element in enumerate(preferredOrder)}
   preferredOrderLen = len(preferredOrder)

   #
   # Now we call sorted() with a `key` function that takes an element (inputElement) in inputList and returns the key to
   # use for sorting purposes.  In our case, our key we return is a pair, (preferredIndex, inputElement), where
   # preferredIndex is either
   #      - the index in preferredOrder of inputElement, if the item was found in preferredOrderIndexLookup
   #      - one more than the highest index in preferredOrder
   #
   # Since the key is a pair, it sorts as:
   #    (A1, B1) < (A2, B2)  <=>  A1 < A2  or  A1 == A2 and B1 < B2
   #
   return sorted(
      inputList,
      key=lambda inputElement: (preferredOrderIndexLookup.get(inputElement, preferredOrderLen), inputElement)
   )

#
# Parse command line arguments
#
parser = argparse.ArgumentParser()
parser.add_argument("-v",
                    "--verbose",
                    action = 'store_true',
                    help = "Turn on debugging messages (which go to stderr)")
args = parser.parse_args()

#
# This is doubtless not totally bulletproof, but at least make an effort to ensure current directory is 'scripts', so
# that references to '../docs' below are valid.
#
sourceFile = os.path.abspath(inspect.getsourcefile(lambda:0))
print(f"Running {sourceFile} to generate DotBeer documentation from schema")
sourceDir = os.path.dirname(sourceFile)
os.chdir(sourceDir)
print(f"Current directory now {os.getcwd()}")

os.makedirs("../docs", exist_ok=True)

topLevelMd = ""
footerMarkdown = ""
timeAndDateNowUtc = datetime.now(timezone.utc)
timeAndDateLocal = timeAndDateNowUtc.astimezone()
dateStamp = timeAndDateLocal.strftime('%Y-%m-%d')
timeStamp = timeAndDateLocal.strftime('%H:%M:%S%z')

#
# To keep things easily digestible for readers, we generate one documentation Markdown file for each schema file.
# As we're going along, we'll also generate the contents of top-level index file that lists all the other ones.
#

#
# Although we list the file order here (for the INDEX document), we make sure we pick up all the schema files, including
# any not listed here.  This means that, if we add a new schema file but forget to add it to the list here, it will
# still get included in the documentation.
#
# Since we'd like to group things together in the INDEX document, we have headings as well as files in this list.
# Headings begin with '>'.  Note however that the first item in this list cannot be a heading.  (This restriction makes
# the code below simpler, and doesn't really tie our hands as we already have special processing for the DotBeer file.)
#
preferredOrder = [
   "DotBeer",
   ">Ingredients",
   "Fermentable", "Hop", "MiscIngredient", "Culture",
   #"WaterAdjustment",
   ">Processes",
   "Mash", "Boil", "Fermentation", "StepCommon",
   ">Other freestanding elements used in a recipe",
   "Style", "Equipment", "Water",
   ">Recipe is best read or written after all above (see note below)",
   "Recipe",
   ">Other",
   "Measurement"
]

#
# We create a merged list of the hard-coded files and headings above plus any files in the schema directory that were
# not in that list.  (Going via `set` removes duplicates.)   Then we sort the combined list to match the order of
# preferredOrder above.  This is obviously far from being optimal, but the lists are short in absolute terms and this
# script is only run occasionally, so it doesn't matter.
#
baseNames = list(
   set(
      preferredOrder +
      [os.path.basename(schemaFile).removesuffix(".beer.schema") for schemaFile in glob.glob("../schema/*.beer.schema")]
   )
)

orderedBaseNames = sortWithPreference(baseNames, preferredOrder)
dotBeerSchemaVersion = ""
for baseName in orderedBaseNames:

   if not baseName.startswith(">"):
      # It seems silly that we had schemaFile (in the output of glob.glob) and need to recreate it here, but it's not a
      # huge overhead and feels less clunky than the alternatives.
      schemaFile = f"../schema/{baseName}.beer.schema"
      docFile = f"../docs/{baseName}.md"
      print(f"Parsing {schemaFile} to {docFile}")
      schema = JsoncParser.parse_file(schemaFile)

      if (baseName == "DotBeer"):
         dotBeerSchemaVersion = schema.get("Version")
         footerMarkdown = (
            #
            # There isn't AFAICT a neat way to do footers in Markdown (though you can do footnotes).  This is the poor
            # man's version.  Note that, although some folks will suggest you use an HTML <footer> tag, this is (a) not
            # supported by all Markdown readers and (b) breaks the links in the webpages generated by Jekyll from our
            # Markdown.
            #
            f"\n\n---\n\n"
            "Documentation generated from the "
            f"[DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v{dotBeerSchemaVersion}) "
            f"on {dateStamp} at {timeStamp}."
         )

         topLevelMd = (
            f"# DotBeer {dotBeerSchemaVersion}\n\n"
            "A DotBeer (<span style=\"color:green; font-weight: bold; font-family: monospace;\">.beer</span>) file is a "
            "JSONC (JSON with comments allowed) document with a `DotBeer` root element.  A <span style=\"color:green; "
            "font-weight: bold; font-family: monospace;\">.beer</span> should be validated against the DotBeer schema "
            "before being read.  The schema is split into the following sections (with a corresponding <span "
            "style=\"color:BlueViolet; font-weight: bold; font-family: monospace;\">.beer.schema</span> file for each "
            "one):\n\n"
            "#### Root element\n\n"
         )
      topLevelMd += f"  - [{baseName}]({docFile})\n"

      schemaBase = os.path.abspath(schemaFile)
      jsm_kwargs = {
         "title": baseName,
         "dotBeerSchemaVersion": dotBeerSchemaVersion,
         "footerMarkdown": footerMarkdown,
         "replace_refs": False,
         "debug": args.verbose,  # Turning this on sends log messages to stderr
         "hide_empty_columns": True,
         "examples_format": "text",
         "sort_yaml_keys": False,
      }

      markdown = markdownGenerator.generate(schema, **jsm_kwargs)
      with open(docFile, "w") as document:
         document.write(markdown)
   else:
      topLevelMd += f"\n#### {baseName.removeprefix(">")}\n\n"

with open("../docs/INDEX.md", "w") as indexFile:
   indexFile.write(topLevelMd)
   indexFile.write(
      "\nWhen reading or writing a <span style=\"color:green; font-weight: bold; font-family: monospace;\">.beer</span>"
      " file, we recommend you read or write `Recipe` record(s) after all the ingredients, processes and so on that "
      "the recipes refer to.  This is because, inside the `Recipe` record, there is enough information to eg identify "
      "each hop added to the recipe, but not all the information to recreate that hop record if it is not already "
      "present on the system reading the record.\n\n"
      "The version of the DotBeer schema is stored in the `Version` field in the <span style=\"color:BlueViolet; "
      "font-weight: bold; font-family: monospace;\">DotBeer.beer.schema</span> file.  Versions prior to 1.0.0 are "
      "subject to breaking changes, but from 1.0.0 onwards adhere to the backwards compatibility principle.  This "
      "principle is that you should always be able to validate an older <span style=\"color:green; font-weight: bold; "
      "font-family: monospace;\">.beer</span> file against a newer schema (although the reverse is not guaranteed).  "
      "Eg, if a file were written using the 1.0.0 schema, it should validate and be readable against the 1.1.0 "
      "schema.\n\n"
      "If a field is marked `deprecated` in the schema that usually means it should be supported for reading but not "
      "for writing.  This approach is part of what maintains the backwards compatibility principle."
   )
   indexFile.write(footerMarkdown)

print('Done')