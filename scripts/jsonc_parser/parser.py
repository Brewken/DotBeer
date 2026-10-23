#=======================================================================================================================
# scripts/jsonc_parser/parser.py is part of dotBeer and is copyright the following authors 2021-2026:
#   • Nickolai Beloguzov <nickolai.beloguzov@gmail.com>
#   • Matt Young <mfsy@yahoo.com>
#
# This file is derived from jsonc-parser release 1.1.5 (https://github.com/NickolaiBeloguzov/jsonc-parser), which is
# distributed under the MIT License (see NOTICE).  Changes from the original are marked with comments.
#
# This Source Code Form is subject to the terms of the Mozilla Public License (MPL), version 2.0.  If a copy of the MPL
# was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# DotBeer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Mozilla Public License for more details.
#=======================================================================================================================
import json
import re
from jsonc_parser.errors import FileError, FunctionParameterError, ParserError
import os
from typing import Union


class JsoncParser:

    #
    # *** Modification to upstream code ***
    # We replace the following line:
    #    regex = re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE | re.DOTALL)
    # as it doesn’t understand \" inside strings
    #
    # Group 1 matches a complete JSON string literal, correctly skipping over escaped characters (eg \" or \\) so that a
    # `//` or `/*` inside a string is never mistaken for the start of a comment.  Group 2 matches a comment.  Because
    # re.sub scans left to right, whichever of the two starts first wins, which is exactly what we want.
    #
    # NB: JSON does not have single-quoted strings, so, unlike the upstream version, we do not try to match them.
    #
    # This is raised upstream as https://github.com/NickolaiBeloguzov/jsonc-parser/issues/12
    #
    regex = re.compile(r'("(?:\\.|[^"\\])*")|(/\*.*?\*/|//[^\r\n]*$)', re.MULTILINE | re.DOTALL)

    #
    # *** Modification to upstream code ***
    # Upstream also has `newline_replace_regex = re.compile("\n{2,}", re.MULTILINE)`, which is never used, so we have
    # removed it.
    #

    @staticmethod
    def _strip_comments(text: str) -> str:
        """
        *** Modification to upstream code ***
        Upstream deletes each comment outright.  For a multi-line /* ... */ comment, that also deletes the newlines
        inside it, so the line numbers in any error message from json.loads() no longer match the file -- which makes
        it much harder to find the problem.  Instead, we replace each comment with spaces, keeping any line breaks, so
        that every character after it stays at the same line and column.
        """
        def replace(match: re.Match) -> str:
            if match.group(2) is not None:
                return re.sub(r"[^\r\n]", " ", match.group(2))
            return match.group(1)

        return JsoncParser.regex.sub(replace, text)

    #
    # *** Modification to upstream code ***
    # Python's json module, by default, (a) silently keeps the last value when an object has a duplicate key and (b)
    # accepts NaN, Infinity and -Infinity, which are not valid JSON.  dotBeer forbids both (see "File format details" in
    # README.md), and JSON Schema validation cannot catch either (because it only sees the parsed result), so we reject
    # them here.
    #
    @staticmethod
    def _reject_duplicate_keys(pairs: list) -> dict:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate key \"{}\" in object".format(key))
            result[key] = value
        return result

    @staticmethod
    def _reject_constant(name: str):
        raise ValueError("{} is not valid JSON (numbers must be finite)".format(name))

    @staticmethod
    def _loads(text: str):
        return json.loads(JsoncParser._strip_comments(text),
                          object_pairs_hook=JsoncParser._reject_duplicate_keys,
                          parse_constant=JsoncParser._reject_constant)

    @staticmethod
    def parse_str(_string: str) -> dict:
        """
        Parse JSON-as-string and deserialize its content into Python dictionary,
        ignoring any comments.

        Parameters: `_string:str` - path to file

        This function will raise a `FunctionParameterError` exception if `_string` parameter
        has an incorrect type or is empty.
        This function will raise a `ParserError` exception if the string cannot be parsed.
        This function will raise any additional exceptions if occurred.
        """
        #
        # *** Modification to upstream code ***
        # Upstream does not mark this as a @staticmethod (which works when called as JsoncParser.parse_str(...), but
        # not when called on an instance), applies the regex substitution twice (once is enough), and includes the
        # whole of the input string in the error message (which, for a file-sized string, buries the actual error).
        #
        if type(_string) != str:
            raise FunctionParameterError(
                "_string parameter must be str; got {} instead".format(type(_string).__name__)
            )

        try:
            return JsoncParser._loads(_string)
        except Exception as e:
            raise ParserError("string cannot be parsed (message: {})".format(str(e))) from e

    @staticmethod
    def parse_file(filepath: Union[str, os.PathLike]) -> dict:
        """
        Parse .jsonc file and deserialize its content into Python dictionary,
        ignoring any comments.

        Parameters: `filepath: str | os.PathLike` - path to file

        This function will raise a `FunctionParameterError` exception if `filepath` parameter
        has an incorrect type or is empty.
        This function will raise a `FileError` exception if the file does not exist.
        This function will raise a `ParserError` exception if file cannot be parsed.
        This function will raise any additional exceptions if occurred.
        """
        # verify that provided path is a valid path-like object
        try:
            filepath = os.fspath(filepath)
        except TypeError:
            #
            # *** Modification to upstream code ***
            # Upstream has `type(path)` here, which raises NameError (there is no `path` variable).  If os.fspath()
            # throws, filepath has not been reassigned, so it still holds what we were given.
            #
            raise FunctionParameterError(
                "filepath parameter must be path-like; got {} instead".format(type(filepath).__name__)
            )

        if not filepath:
            raise FunctionParameterError("path is empty.")

        if not os.path.isfile(filepath):
            raise FileError("{} does not exist or is not a file".format(filepath))

        #
        # *** Modification to upstream code ***
        # Upstream rejects files whose extension is not .json or .jsonc, which would stop us reading .beer and
        # .beer.schema files.  We have removed that check.  (Raised upstream as
        # https://github.com/NickolaiBeloguzov/jsonc-parser/issues/9.)
        #

        #
        # *** Modification to upstream code ***
        # Explicitly read as UTF-8.  Otherwise Python uses the locale's encoding, which is not UTF-8 on, eg, Windows,
        # and our schema files contain non-ASCII characters (•, °, ₂, etc).
        #
        with open(filepath, "r", encoding="utf-8") as json_file:
            data_raw = json_file.read()

        try:
            return JsoncParser._loads(data_raw)
        except Exception as e:
            raise ParserError("{} file cannot be parsed (message: {})".format(filepath, str(e))) from e

    #
    # *** Modification to upstream code ***
    # convert_to_json() and convert_to_jsonc() are not used by dotBeer, but we keep them, with the following fixes:
    #  - Upstream (in convert_to_jsonc) has `type(path)` in an error message, which raises NameError
    #  - Upstream deletes the source file (if asked to) *before* checking whether the output file already exists, so,
    #    if it does, the source file is lost and nothing is written.  We now check first.
    #  - Upstream does not specify an encoding when writing (see comment in parse_file())
    #
    @staticmethod
    def _convert(filepath: Union[str, os.PathLike], remove_file: bool, new_extension: str) -> None:
        # verify that provided path is a valid path-like object
        try:
            filepath = os.fspath(filepath)
        except TypeError:
            raise FunctionParameterError(
                "filepath parameter must be path-like; got {} instead".format(type(filepath).__name__)
            )

        if not filepath:
            raise FunctionParameterError("path is empty.")

        if type(remove_file) != bool:
            raise FunctionParameterError(
                "remove_file parameter must be bool; got {} instead.".format(
                    type(remove_file).__name__
                )
            )

        data = JsoncParser.parse_file(filepath)

        new_filename = os.path.splitext(filepath)[0] + new_extension
        if os.path.exists(new_filename):
            raise FileError("{} file already exists".format(new_filename))

        with open(new_filename, "x", encoding="utf-8") as json_file:
            json_file.write(json.dumps(data, indent=2, ensure_ascii=False))

        if remove_file:
            os.remove(filepath)

    @staticmethod
    def convert_to_json(filepath: Union[str, os.PathLike], remove_file: bool = False) -> None:
        """
        Convert file from .jsonc to .json format, removing any comments from it

        Parameters: `path: str | os.PathLike` is a path to file, `remove_file:bool` indicates if
        source file will be deleted or not. If set to True, .jsonc file will be deleted from the
        hard drive, otherwise file remains alongside with its .json output.

        This function will raise a `FunctionParameterError` if one or more of function's parameters
        has an incorrect type/invalid value.
        This function will raise any additional exceptions if occurred.

        """
        JsoncParser._convert(filepath, remove_file, ".json")

    @staticmethod
    def convert_to_jsonc(filepath: Union[str, os.PathLike], remove_file: bool = False):
        """
        Convert file .jsonc format, enabling comments.

        Parameters: `filepath: str | os.PathLike` is a path to file, `remove_file:bool` indicates
        if source file will be deleted or not. If set to True, .json file will be deleted from the
        hard drive, otherwise file remains alongside with its .jsonc output.

        This function will raise a `FunctionParameterError` if one or more of function's parameters
        has an incorrect type/invalid value.
        This function will raise any additional exceptions if occurred.
        """
        JsoncParser._convert(filepath, remove_file, ".jsonc")
