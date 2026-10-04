# DotBeer

Root element of all DotBeer documents.  Most of the Primary Types (ie ones that have their own schema file) are referred to here.  Various Component Types (ie smaller types used for composition) are defined in the "$defs" sections of most of the schema files (apart from this one).

<strong>DotBeer</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| version | ✅ | [VersionNumber](#versionnumber) | DotBeer schema version used to create the file. |
| output_by | ✅ | string | Application that wrote the file -- eg Brewtarget 5.2.1. |
| timestamp | ✅ | [Measurement::Date](./Measurement.md#date) | Date and time file was created. |
| hops |  | array of [Hop](./Hop.md) | Records detailing properties of unique hop varieties. |
| fermentables |  | array of [Fermentable](./Fermentable.md) | Records for any ingredient that contributes to the gravity of the beer. |
| miscs |  | array of [Misc](./Misc.md) | Records for ingredients that area not hops, fermentables or cultures.  Variously known as "miscellaneous ingredients", "non-fermentable adjuncts", "other ingredients", or "adjuncts that do not contribute to the gravity of the beer". |
| cultures |  | array of [Culture](./Culture.md) | Records detailing the wide array of unique cultures. |
| waters |  | array of [Water](./Water.md) | Records for water profiles used in brewing. |
| mashes |  | array of [Mash](./Mash.md) | Common mashing procedures. |
| boils |  | array of [Boil](./Boil.md) | Common boil procedures. |
| fermentations |  | array of [Fermentation](./Fermentation.md) | Common fermentation procedures. |
| styles |  | array of [Style](./Style.md) | Details of judging guidelines for individual beer styles. |
| equipments |  | array of [Equipment](./Equipment.md) | Provides necessary information for brewing equipment. |
| recipes |  | array of [Recipe](./Recipe.md) | Records containing a minimal collection of the description of ingredients, procedures and other required parameters necessary to recreate a batch of beer. |


---

# Component Types

## FolderPath

A FolderPath is typically used for the suggested slash-delimited subfolder path in which to store an object.  Any leading slash should be ignored.  Eg, if an object's folder path is "/hum/bug" (or "hum/bug") then importing the object into folder "/foo/bar" should result in its folder path being "/foo/bar/hum/bug".  If the importing software does not support folders, then it should ignore folder path fields.

<strong>FolderPath</strong> is a ``string``  matching regular expression [`^[/]?([^/]+([/][^/]+)*)?$`](https://regex101.com/?regex=%5E%5B%2F%5D%3F%28%5B%5E%2F%5D%2B%28%5B%2F%5D%5B%5E%2F%5D%2B%29%2A%29%3F%24)

## LocalId

A string that, within a dotBeer file, uniquely identifies something (eg hop, fermentable, style, mash) that is used in a recipe in that same file.  Thus, for example, if each hop in the file defines its own local ID, then, for the hop additions in any recipe in the same file, it suffices to use the relevant local ID to identify the hop being added.

No two items in a single file should have the same local ID, even if they are of different types.  (This is to make reading files simpler, as a single look-up map can be used for all different types.)  The string has no meaning in any wider scope: it is a cross-reference rather than a true attribute.  Local IDs simplify the structure of dotBeer and help reduce repetition within the files.

The JSON Schema cannot validate that local IDs are correct - merely that they adhere to a particular format.  Implementing programs should therefore validate that (a) all defined local IDs in a file are unique in that file, (b) all referred-to local IDs are defined elsewhere in the file, and (c) any referred-to local ID is for an object of the relevant type (eg the local ID for the style of a recipe must be that of a style).

<strong>LocalId</strong> is a ``string``  matching regular expression [`[A-Za-z0-9_]+`](https://regex101.com/?regex=%5BA-Za-z0-9_%5D%2B)

## VersionNumber

We use semantic versioning, which encodes a version by a three-part version number (Major.Minor.Patch)

<strong>VersionNumber</strong> is a ``string``  matching regular expression [`\d+[.]\d+[.]\d+`](https://regex101.com/?regex=%5Cd%2B%5B.%5D%5Cd%2B%5B.%5D%5Cd%2B)



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.7.0) on 2026-10-04 at 09:57:34+0200.
