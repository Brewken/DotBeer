# DotBeer File Format

A free and open serialisation format for beer recipes, ingredients and related data

<strong>DotBeer File Format</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | -------- | --------------- | ----------- |
| DotBeer | ✅ | object | Root element of all DotBeer documents. |
| DotBeer.version | ✅ | [Measurement::VersionNumber](./Measurement.md#versionnumber) | DotBeer schema version used to create the file. |
| DotBeer.output_by | ✅ | string | Application that wrote the file -- eg Brewtarget 5.2.1. |
| DotBeer.timestamp | ✅ | [Measurement::Date](./Measurement.md#date) | Date and time file was created. |
| DotBeer.hops |  | [Hop](./Hop.md) | Records detailing properties of unique hop varieties. |
| DotBeer.fermentables |  | [Fermentable](./Fermentable.md) | Records for any ingredient that contributes to the gravity of the beer. |
| DotBeer.other_ingredients |  | [OtherIngredient](./OtherIngredient.md) | Records for adjuncts which do not contribute to the gravity of the beer. |
| DotBeer.cultures |  | [Culture](./Culture.md) | Records detailing the wide array of unique cultures. |
| DotBeer.waters |  | [Water](./Water.md) | Records for water profiles used in brewing. |
| DotBeer.mashes |  | [Mash](./Mash.md) | Common mashing procedures. |
| DotBeer.boils |  | [Boil](./Boil.md) | Common boil procedures. |
| DotBeer.fermentations |  | [Fermentation](./Fermentation.md) | Common fermentation procedures. |
| DotBeer.styles |  | [Style](./Style.md) | Details of judging guidelines for individual beer styles. |
| DotBeer.equipments |  | [Equipment](./Equipment.md) | Provides necessary information for brewing equipment. |
| DotBeer.recipes |  | [Recipe](./Recipe.md) | Records containing a minimal collection of the description of ingredients, procedures and other required parameters necessary to recreate a batch of beer. |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
