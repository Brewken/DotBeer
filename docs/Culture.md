# Culture

Collects the attributes of a microbial culture such as a yeast.

<strong>Culture</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| culture_type | ✅ | Enum:<br>&nbsp;∙ `ale`<br>&nbsp;∙ `bacteria`<br>&nbsp;∙ `brett`<br>&nbsp;∙ `champagne`<br>&nbsp;∙ `kveik`<br>&nbsp;∙ `lacto`<br>&nbsp;∙ `lager`<br>&nbsp;∙ `malolactic`<br>&nbsp;∙ `mixed-culture`<br>&nbsp;∙ `other`<br>&nbsp;∙ `pedio`<br>&nbsp;∙ `spontaneous`<br>&nbsp;∙ `wine` |  |
| form | ✅ | Enum:<br>&nbsp;∙ `liquid`<br>&nbsp;∙ `dry`<br>&nbsp;∙ `slant`<br>&nbsp;∙ `culture`<br>&nbsp;∙ `dregs` |  |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this Culture object. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Culture object. |
| producer |  | string |  |
| product_id |  | string |  |
| temperature_range |  | [Measurement::RangeOfTemperature](./Measurement.md#rangeoftemperature) | The recommended temperature range of fermentation by the culture producer. |
| alcohol_tolerance |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The recommended limit of abv by the culture producer before attenuation stops. |
| flocculation |  | Enum:<br>&nbsp;∙ `very low`<br>&nbsp;∙ `low`<br>&nbsp;∙ `medium low`<br>&nbsp;∙ `medium`<br>&nbsp;∙ `medium high`<br>&nbsp;∙ `high`<br>&nbsp;∙ `very high` | Flocculation refers to the ability of yeast to aggregate to form large flocs which drop out of suspension. |
| attenuation_range |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) |  |
| notes |  | string |  |
| best_for |  | string | Recommended styles for a particular culture. |
| max_reuse |  | `0 <= x ` | Maximum number of times to reuse a culture before a new lab source is recommended. |
| pof |  | boolean | A POF+ culture is capable of producing phenols, which is a common distinctive property of saison, and brett yeasts. |
| glucoamylase |  | boolean | A glucoamylase positive culture is capable of producing glucoamylase, the enzyme produced through expression of the diastatic gene, which allows yeast to attenuate dextrins and starches leading to a very low FG. This is positive in some saison/brett yeasts as well as the new gulo hybrid by Omega yeast labs. |
| inventory |  | [CultureAmount](#cultureamount) |  |
| killer |  | [KillerProperties](#killerproperties) |  |


---

# Component Types

## CultureAmount

The ways in which an amount of a Culture could be measured

## KillerProperties

Killer yeast properties (also known as zymocide) are common among wine yeasts.  There are some ale and brett yeasts that are immune to some killer (aka zymocidic) properties, these are known as "killer neutral".

See https://www.milkthefunk.com/wiki/Saccharomyces#Killer_Wine_Yeast for more on "killer" yeasts and "killer neutral" yeasts.  Some folks call these killer yeast properties "zymocide", but AFAICT "killer" is still the more widely used term, at least in relation to brewing.

Note that `neutral` being `true` implies all the other `producingXxxToxin` properties are `false`, because "neutral strains do not produce toxins, nor are they killed by them".

<strong>KillerProperties</strong> is a JSON object with the following properties:

| Property | Required? | Type | Conditional? |
| -------- | --------- | ---- | ------------ |
| producing_K1_toxin |  | boolean |  |
| producing_K1_toxin |  | `False` | **If** neutral = True |
| producing_K2_toxin |  | boolean |  |
| producing_K2_toxin |  | `False` | **If** neutral = True |
| producing_K28_toxin |  | boolean |  |
| producing_K28_toxin |  | `False` | **If** neutral = True |
| producing_Klus_toxin |  | boolean |  |
| producing_Klus_toxin |  | `False` | **If** neutral = True |
| neutral |  | boolean |  |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.8.0) on 2026-10-07 at 21:37:28+0200.
