#=======================================================================================================================
# scripts/jsonc_parser/errors.py is part of dotBeer and is copyright the following authors 2021-2026:
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
class FunctionParameterError(Exception):
    """
    This excption indicates that one or more of function's parameters are incorrect
    """

    def __init__(self, *args):
        self.__msg = args[0]
        super().__init__(self.__msg)

    def __str__(self):
        return self.__msg


class FileError(Exception):
    """
    This exception indicates that file format cannot be parsed
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class ParserError(Exception):
    """
    This exception indicates that file cannot be parsed
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()