# DotBeer

Root element of all DotBeer documents.  Most of the Primary Types (ie ones that have their own schema file) are referred to here.  Various Component Types (ie smaller types used for composition) are defined in the "$defs" sections of most of the schema files (apart from this one).

<strong>DotBeer</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| version | ✅ | [Measurement::VersionNumber](./Measurement.md#versionnumber) | DotBeer schema version used to create the file. |
| output_by | ✅ | string | Application that wrote the file -- eg Brewtarget 5.2.1. |
| timestamp | ✅ | [Measurement::Date](./Measurement.md#date) | Date and time file was created. |
| hops |  | array of [Hop](./Hop.md) | Records detailing properties of unique hop varieties. |
| fermentables |  | array of [Fermentable](./Fermentable.md) | Records for any ingredient that contributes to the gravity of the beer. |
| misc_ingredients |  | array of [MiscIngredient](./MiscIngredient.md) | Records for ingredients that area not hops, fermentables or cultures.  Variously known as "miscellaneous ingredients", "non-fermentable adjuncts", "other ingredients", or "adjuncts that do not contribute to the gravity of the beer". |
| cultures |  | array of [Culture](./Culture.md) | Records detailing the wide array of unique cultures. |
| waters |  | array of [Water](./Water.md) | Records for water profiles used in brewing. |
| mashes |  | array of [Mash](./Mash.md) | Common mashing procedures. |
| boils |  | array of [Boil](./Boil.md) | Common boil procedures. |
| fermentations |  | array of [Fermentation](./Fermentation.md) | Common fermentation procedures. |
| styles |  | array of [Style](./Style.md) | Details of judging guidelines for individual beer styles. |
| equipments |  | array of [Equipment](./Equipment.md) | Provides necessary information for brewing equipment. |
| recipes |  | array of [Recipe](./Recipe.md) | Records containing a minimal collection of the description of ingredients, procedures and other required parameters necessary to recreate a batch of beer. |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.4.0) on 2026-08-08 at 19:08:56+0200.
