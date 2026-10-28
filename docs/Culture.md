# Culture

Collects the attributes of a microbial culture such as a yeast.

<strong>Culture</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string | Name of the culture, usually the name its producer sells it under. |
| culture_type | ✅ | Enum:<br>&nbsp;∙ `ale`<br>&nbsp;∙ `bacteria`<br>&nbsp;∙ `brett`<br>&nbsp;∙ `champagne`<br>&nbsp;∙ `kveik`<br>&nbsp;∙ `lacto`<br>&nbsp;∙ `lager`<br>&nbsp;∙ `malolactic`<br>&nbsp;∙ `mixed-culture`<br>&nbsp;∙ `other`<br>&nbsp;∙ `pedio`<br>&nbsp;∙ `spontaneous`<br>&nbsp;∙ `wheat`<br>&nbsp;∙ `wine` | The kind of organism the culture is, which determines how it ferments and what flavours it contributes. |
| form | ✅ | Enum:<br>&nbsp;∙ `liquid`<br>&nbsp;∙ `dry`<br>&nbsp;∙ `slant`<br>&nbsp;∙ `culture`<br>&nbsp;∙ `dregs` | The physical form the culture is supplied or stored in. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this Culture object. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Culture object. |
| producer |  | string | The lab or company that produced the culture. |
| product_id |  | string | Producer’s product code or number for this item. |
| temperature_range |  | [Measurement::RangeOfTemperature](./Measurement.md#rangeoftemperature) | The recommended temperature range of fermentation by the culture producer. |
| alcohol_tolerance |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The recommended limit of abv by the culture producer before attenuation stops.<br /><br />This field is normally only meaningful for yeasts (not bacteria). |
| flocculation |  | Enum:<br>&nbsp;∙ `very low`<br>&nbsp;∙ `low`<br>&nbsp;∙ `medium low`<br>&nbsp;∙ `medium`<br>&nbsp;∙ `medium high`<br>&nbsp;∙ `high`<br>&nbsp;∙ `very high` | Flocculation refers to the ability of yeast to aggregate to form large flocs which drop out of suspension.<br /><br />This field is normally only meaningful for yeasts (not bacteria). |
| attenuation_range |  | [Measurement::RangeOfPercentageNoMax](./Measurement.md#rangeofpercentagenomax) | The range of apparent attenuation that the producer quotes for the culture.  (This can be more than 100%, eg for a diastatic yeast.) |
| notes |  | string |  |
| best_for |  | string | Recommended styles for a particular culture. |
| max_reuse |  | `0 <= x ` | Maximum number of times to reuse a culture before a new lab source is recommended. |
| pof |  | boolean | Phenolic off-flavour positive: converts ferulic acid to 4-vinyl guaiacol (clove), typical of weizen, saison and many Belgian strains.  A POF+ culture is capable of producing phenols, which is a common distinctive property of saison, and brett yeasts.<br /><br />This field is normally only meaningful for yeasts (not bacteria). |
| glucoamylase |  | boolean | STA1-positive (‘diastaticus’): secretes glucoamylase so can ferment dextrins and starch.  Risk of very low FG, over-carbonation and cross-contamination.<br /><br />This field is normally only meaningful for yeasts (not bacteria). |
| killer |  | [KillerProperties](#killerproperties) | Information about any "killer yeast properties".<br /><br />This field is normally only meaningful for yeasts (not bacteria). |


---

# Component Types

## CultureAmount

The ways in which an amount of a Culture could be measured

## KillerProperties

Killer yeast properties (also known as zymocide) are common among wine yeasts.  There are some ale and brett yeasts that are immune to some killer (aka zymocidic) properties, these are known as "killer neutral".

See https://www.milkthefunk.com/wiki/Saccharomyces#Killer_Wine_Yeast for more on "killer" yeasts and "killer neutral" yeasts.  Some folks call these killer yeast properties "zymocide", but AFAICT "killer" is still the more widely used term, at least in relation to brewing.

Note that `neutral` being `true` implies all the other `producing_xxx_toxin` properties are `false`, because "neutral strains do not produce toxins, nor are they killed by them".

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

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.0.0) on 2026-10-28 at 19:46:10+0100.
