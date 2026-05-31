# DotBeer

Root element of all DotBeer documents.

<strong>DotBeer</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| version | ✅ | [Measurement::VersionNumber](./Measurement.md#versionnumber) | DotBeer schema version used to create the file. |
| output_by | ✅ | string | Application that wrote the file -- eg Brewtarget 5.2.1. |
| timestamp | ✅ | [Measurement::Date](./Measurement.md#date) | Date and time file was created. |
| hops |  | array of [Hop](./Hop.md) | Records detailing properties of unique hop varieties. |
| fermentables |  | array of [Fermentable](./Fermentable.md) | Records for any ingredient that contributes to the gravity of the beer. |
| other_ingredients |  | array of [OtherIngredient](./OtherIngredient.md) | Records for adjuncts which do not contribute to the gravity of the beer. |
| cultures |  | array of [Culture](./Culture.md) | Records detailing the wide array of unique cultures. |
| waters |  | array of [Water](./Water.md) | Records for water profiles used in brewing. |
| mashes |  | array of [Mash](./Mash.md) | Common mashing procedures. |
| boils |  | array of [Boil](./Boil.md) | Common boil procedures. |
| fermentations |  | array of [Fermentation](./Fermentation.md) | Common fermentation procedures. |
| styles |  | array of [Style](./Style.md) | Details of judging guidelines for individual beer styles. |
| equipments |  | array of [Equipment](./Equipment.md) | Provides necessary information for brewing equipment. |
| recipes |  | array of [Recipe](./Recipe.md) | Records containing a minimal collection of the description of ingredients, procedures and other required parameters necessary to recreate a batch of beer. |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31 at 18:29:03+0200.
