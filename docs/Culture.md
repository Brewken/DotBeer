# Culture

Collects the attributes of a microbial culture such as a yeast.

<strong>Culture</strong> is a JSON object with all properties from [CultureBase](#culturebase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | -------- | --------------- | ----------- |
| temperature_range |  | [Measurement::RangeOfTemperature](./Measurement.md#rangeoftemperature) | The recommended temperature range of fermentation by the culture producer. |
| alcohol_tolerance |  | [Measurement::Percentage](./Measurement.md#percentage) | The recommended limit of abv by the culture producer before attenuation stops. |
| flocculation |  | Enum:<br>&nbsp;∙ `very low`<br>&nbsp;∙ `low`<br>&nbsp;∙ `medium low`<br>&nbsp;∙ `medium`<br>&nbsp;∙ `medium high`<br>&nbsp;∙ `high`<br>&nbsp;∙ `very high` | Floculation refers to the ability of yeast to aggregate to form large flocs which drop out of suspension. |
| attenuation_range |  | [Measurement::RangeOfPercentage](./Measurement.md#rangeofpercentage) |  |
| notes |  | string |  |
| best_for |  | string | Recommended styles for a particular culture. |
| max_reuse |  | integer | Maximum number of times to reuse a culture before a new lab source is recommended. |
| pof |  | boolean | A POF+ culture is capable of producing phenols, which is a common distinctive property of saison, and brett yeasts. |
| glucoamylase |  | boolean | A glucoamylase positive culture is capable of producing glucoamylase, the enzyme produced through expression of the diastatic gene, which allows yeast to attenuate dextrins and starches leading to a very low FG. This is positive in some saison/brett yeasts as well as the new gulo hybrid by Omega yeast labs. |
| inventory |  | [CultureInventory](#cultureinventory) |  |
| zymocide |  | object | Zymocide, also known as killer yeast properties, is common among wine yeasts. There are also some ale and brett yeasts that are immune to some zymocidic properties, these are known as killer neutral. |
| zymocide.no1 |  | boolean |  |
| zymocide.no2 |  | boolean |  |
| zymocide.no28 |  | boolean |  |
| zymocide.klus |  | boolean |  |
| zymocide.neutral |  | boolean |  |


---

# Definitions

## CultureBase

Provides unique properties to identify individual records of a culture.

<strong>CultureBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | -------- | --------------- |
| name | ✅ | string |
| culture_type | ✅ | Enum:<br>&nbsp;∙ `ale`<br>&nbsp;∙ `bacteria`<br>&nbsp;∙ `brett`<br>&nbsp;∙ `champagne`<br>&nbsp;∙ `kveik`<br>&nbsp;∙ `lacto`<br>&nbsp;∙ `lager`<br>&nbsp;∙ `malolactic`<br>&nbsp;∙ `mixed-culture`<br>&nbsp;∙ `other`<br>&nbsp;∙ `pedio`<br>&nbsp;∙ `spontaneous`<br>&nbsp;∙ `wine` |
| form | ✅ | Enum:<br>&nbsp;∙ `liquid`<br>&nbsp;∙ `dry`<br>&nbsp;∙ `slant`<br>&nbsp;∙ `culture`<br>&nbsp;∙ `dregs` |
| producer |  | string |
| product_id |  | string |

## CultureInventory

No description provided for this model.

<strong>CultureInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | -------- | --------------- |
| liquid |  | [Measurement::Volume](./Measurement.md#volume) |
| dry |  | [Measurement::Mass](./Measurement.md#mass) |
| slant |  | [Measurement::Volume](./Measurement.md#volume) |
| culture |  | [Measurement::Volume](./Measurement.md#volume) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
