# Fermentable

Collects the attributes of a fermentable ingredient to store as record information.

<strong>Fermentable</strong> is a JSON object with all properties from [FermentableBase](#fermentablebase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | -------- | --------------- | ----------- |
| notes |  | string |  |
| moisture |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| alpha_amylase |  | number | Where diastatic power gives the total amount of all enzymes, alpha amylase, also known as dextrinizing units, refers to only the total amount of alpa amylase in the malted grain. A value of 25-50 is desirable for base malt. |
| diastatic_power |  | [Measurement::DiastaticPower](./Measurement.md#diastaticpower) | Diastatic power is a measurement of malted grains enzymatic content. A value of 35 Lintner is needed to self convert, while a value of 100 or more is desirable. |
| protein |  | [Measurement::Percentage](./Measurement.md#percentage) | The percentage of protein. Higher values may indicate a possibility of haze, or lautering issues. |
| kolbach_index |  | [Measurement::Percentage](./Measurement.md#percentage) | The Kolbach Index, also known as soluble to total ratio of nitrogen or protein, is used to indicate the degree of malt modification. A value above 35% is desired for simple single infusion mashing, undermodified malt may require multiple step mashes or decoction. |
| max_in_batch |  | [Measurement::Percentage](./Measurement.md#percentage) | The recommended maximum percentage to use in a grain bill. |
| recommend_mash |  | boolean | True if the fermentable must be mashed, false if it can be steeped. |
| inventory |  | [FermentableInventory](#fermentableinventory) |  |
| glassy |  | [Measurement::Percentage](./Measurement.md#percentage) | Used to indicate the 'crystallized' percentage of starches for crystal malts. |
| plump |  | [Measurement::Percentage](./Measurement.md#percentage) | The percentage of grain that masses through sieves with gaps of 7/64 and 6/64, desired values of 80% or higher which indicate plump kernels. |
| half |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| mealy |  | [Measurement::Percentage](./Measurement.md#percentage) | The opposite of glassy, a mealy kernel is one that is not glassy. Base malt should be at least 90%, single step mashes generally require 95% or higher. |
| thru |  | [Measurement::Percentage](./Measurement.md#percentage) | The Percentage of grain that makes it through a thin mesh screen, typically 5/64 inch. Values less than 3% are desired. |
| friability |  | [Measurement::Percentage](./Measurement.md#percentage) | Friability is the measure of a malts ability to crumble during the crush, and is used as an indicator for easy gelatinization of the grain and starches, as well as modification of the malt. Value of 85% of higher indicates a well modified malt and is suitable for single step mashes. Lower values may require a step mash. |
| di_pH |  | [Measurement::Acidity](./Measurement.md#acidity) | The pH of the resultant wort for 1 lb of grain mashed in 1 gallon of distilled water. Used in many water chemistry / mash pH prediction software. |
| viscosity |  | [Measurement::Viscosity](./Measurement.md#viscosity) | The measure of wort viscosity, typically associated with the breakdown of beta-glucans. The higher the viscosity, the greater the need for a glucan rest and the less suitable for a fly sparge. |
| dms_p |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | The amount of DMS precursors, namely S-methyl methionine (SMM) and dimethyl sulfoxide (DMSO) in the malt which convert to dimethyl sulfide (DMS). |
| fan |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Free Amino Nitrogen (FAN) is a critical yeast nutrient. Typical values for base malt is 170. |
| fermentability |  | [Measurement::Percentage](./Measurement.md#percentage) | Fermentability - Used in Extracts to indicate a baseline typical apparent attenuation for a typical medium attenuation yeast. |
| beta_glucan |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Values of 180 or more may suggest a glucan rest and avoiding fly sparging. |


---

# Definitions

## FermentableBase

FermentableBase provides unique properties to identify individual records of fermentable ingredients.

<strong>FermentableBase</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | -------- | --------------- | ----------- |
| name | ✅ | string |  |
| type | ✅ | Enum:<br>&nbsp;∙ `dry extract`<br>&nbsp;∙ `extract`<br>&nbsp;∙ `grain`<br>&nbsp;∙ `sugar`<br>&nbsp;∙ `fruit`<br>&nbsp;∙ `juice`<br>&nbsp;∙ `honey`<br>&nbsp;∙ `other` |  |
| yield | ✅ | object | The potential yield of the fermentable ingredient, supporting SG, or percentage. eg 1.037 or 80% are valid yield types. |
| yield.fine_grind |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage yield, compared to sucrose, of a fine grind. eg 80% |
| yield.coarse_grind |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage yield, compared to sucrose, of a coarse grind. eg 78% |
| yield.fine_coarse_difference |  | [Measurement::Percentage](./Measurement.md#percentage) | The difference between fine and coarse grind, a difference more than 2 percent can indicate a protein or step mash may be desirable. eg 2%. |
| yield.potential |  | [Measurement::Density](./Measurement.md#density) | The potential yield of the fermentable ingredient for 1 lb of grain mashed in 1 gallon of water. eg 1.037 |
| color | ✅ | [Measurement::Color](./Measurement.md#color) |  |
| origin |  | string |  |
| producer |  | string |  |
| product_id |  | string |  |
| grain_group |  | Enum:<br>&nbsp;∙ `base`<br>&nbsp;∙ `caramel`<br>&nbsp;∙ `flaked`<br>&nbsp;∙ `roasted`<br>&nbsp;∙ `specialty`<br>&nbsp;∙ `smoked`<br>&nbsp;∙ `adjunct` |  |

## FermentableInventory

No description provided for this model.

<strong>FermentableInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | -------- | --------------- |
| amount |  | [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
