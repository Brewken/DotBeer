# Culture

Collects the attributes of a microbial culture such as a yeast.

<strong>Culture</strong> is a JSON object with all properties from [CultureBase](#culturebase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
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
| killer |  | [KillerProperties](#killerproperties) |  |


---

# Component Types

## CultureBase

Provides unique properties to identify individual records of a culture.

<strong>CultureBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| name | ✅ | string |
| culture_type | ✅ | Enum:<br>&nbsp;∙ `ale`<br>&nbsp;∙ `bacteria`<br>&nbsp;∙ `brett`<br>&nbsp;∙ `champagne`<br>&nbsp;∙ `kveik`<br>&nbsp;∙ `lacto`<br>&nbsp;∙ `lager`<br>&nbsp;∙ `malolactic`<br>&nbsp;∙ `mixed-culture`<br>&nbsp;∙ `other`<br>&nbsp;∙ `pedio`<br>&nbsp;∙ `spontaneous`<br>&nbsp;∙ `wine` |
| form | ✅ | Enum:<br>&nbsp;∙ `liquid`<br>&nbsp;∙ `dry`<br>&nbsp;∙ `slant`<br>&nbsp;∙ `culture`<br>&nbsp;∙ `dregs` |
| producer |  | string |
| product_id |  | string |

## CultureInventory



<strong>CultureInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| liquid |  | [Measurement::Volume](./Measurement.md#volume) |
| dry |  | [Measurement::Mass](./Measurement.md#mass) |
| slant |  | [Measurement::Volume](./Measurement.md#volume) |
| culture |  | [Measurement::Volume](./Measurement.md#volume) |

## KillerProperties

Killer yeast properties (also known as zymocide) are common among wine yeasts.  There are some ale and brett yeasts that are immune to some killer (aka zymocidic) properties, these are known as "killer neutral".

See https://www.milkthefunk.com/wiki/Saccharomyces#Killer_Wine_Yeast for more on "killer" yeasts and "killer neutral" yeasts.  Some folks call these killer yeast properties "zymocide", but AFAICT "killer" is still the more widely used term, at least in relation to brewing.

Note that `killerNeutral` being `true` implies all the other `producingXxxToxin` properties are `false`, because "neutral strains do not produce toxins, nor are they killed by them".

<strong>KillerProperties</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| producingK1Toxin |  | boolean |
| producingK2Toxin |  | boolean |
| producingK28Toxin |  | boolean |
| producingKlusToxin |  | boolean |
| neutral |  | boolean |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-06-10 at 09:03:35+0200.
