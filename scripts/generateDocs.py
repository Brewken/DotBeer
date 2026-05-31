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

from jsonc_parser.parser import JsoncParser

import markdownGenerator

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

#
# To keep things easily digestible for readers, we generate one documentation markdown file for each schema file
#
schemaFiles = glob.glob("../schema/*.beer.schema")
for schemaFile in schemaFiles:
   baseName = os.path.basename(schemaFile).removesuffix(".beer.schema")
   docFile = f"../docs/{baseName}.md"
   print(f"Parsing {schemaFile} to {docFile}")
   schema = JsoncParser.parse_file(schemaFile)

   schemaBase = os.path.abspath(schemaFile)
   jsm_kwargs = {
      "title": baseName,
      "footer": True,
      "replace_refs": False,
      "debug": args.verbose,  # Turning this on sends log messages to stderr
      "hide_empty_columns": True,
      "examples_format": "text",
      "sort_yaml_keys": False,
   }

   markdown = markdownGenerator.generate(schema, **jsm_kwargs)
   with open(docFile, "w") as document:
      document.write(markdown)

print('Done')