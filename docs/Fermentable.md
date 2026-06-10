# Fermentable

Collects the attributes of a fermentable ingredient to store as record information.

<strong>Fermentable</strong> is a JSON object with all properties from [FermentableBase](#fermentablebase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| notes |  | string |  |
| moisture |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage moisture.  Only appropriate for a "grain" or "other" type |
| alpha_amylase |  | number | Total amount of alpha-amylase in the malted grain, measured in dextrinizing units.  (Since you ask, one α-amylase dextrinizing unit is defined as the quantity of α-amylase that will dextrinize soluble starch in the presence of an excess of β-amylase at the rate of 1 g/h at 30°C.  Or, at least, that's what it says at https://www.deerland.com/wp-content/uploads/2015/04/EnzymeAssayUnits_Deerland.pdf.)  Anyway, a value of 25-50 is desirable for base malt. |
| diastatic_power |  | [Measurement::DiastaticPower](./Measurement.md#diastaticpower) | Diastatic power is a measurement of malted grains enzymatic content. A value of 35 Lintner is needed to self convert, while a value of 100 or more is desirable. |
| protein |  | [Measurement::Percentage](./Measurement.md#percentage) | The percentage of protein. Higher values may indicate a possibility of haze, or lautering issues. |
| kolbach_index |  | [Measurement::Percentage](./Measurement.md#percentage) | The Kolbach Index, also known as soluble to total ratio of nitrogen or protein, is used to indicate the degree of malt modification. A value above 35% is desired for simple single infusion mashing, undermodified malt may require multiple step mashes or decoction. |
| max_in_batch |  | [Measurement::Percentage](./Measurement.md#percentage) | The recommended maximum percentage to use in a grain bill. |
| recommend_mash |  | boolean | True if the fermentable must be mashed, false if it can be steeped. |
| inventory |  | [FermentableInventory](#fermentableinventory) |  |
| glassy |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage of malt that is "glassy".  For a malt, % "glassy" + % "half glassy" + % "mealy" = 100%.<br /><br />From https://byo.com/article/understanding-malt-spec-sheets-advanced-brewing/:<br /><br />Malt is also classified in terms of hardness. By convention, it is described as “mealy,” “half-glassy” and “glassy.” Mealy kernels have an endosperm (the partially germinated portion at the heart of the kernel that contains the starches) that is 25% or less glassy (hard). Glassy kernels have an endosperm that is more than 75% hard. The remaining kernels (26–75% hard) are said to be half-glassy.<br /><br />See also https://www.probrewer.com/library/malt/understanding-malt-analysis-sheets/:<br /><br />By convention, malt is classified by what percentage of the lot is “mealy,” “half-glassy/glassy-ends” and “glassy.”<br />...<br />Any base malt destined for brewing should be at least 90% mealy; if it is to be infusion-mashed it must be at least 95% mealy.  For base malts whose mealiness is expressed as a ratio, mealy/half-glassy/glassy, the ratio should be 92%/7%/1% for decoction and step mashing, and 95%/4%/1% or better for infusion mashing. |
| plump |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage of grain that is "plump". The percentage of grain that masses through sieves with gaps of 7/64″ and 6/64″, desired values of 80% or higher which indicate plump kernels.<br /><br />From https://byo.com/article/understanding-malt-spec-sheets-advanced-brewing/:<br /><br />The kernel size [of the malt] is typically expressed in terms of screen separation, that is, the fraction of kernels that do not pass through screens of various sizes.  In general, larger kernels will exhibit higher extract yields.  Kernels smaller than 2 mm (0.079 in.) can be indications of poor or nonexistent modification.  Sometimes the size value is given only in terms of the percentage of kernels that are “plump” or “thin.”  Malt that is more than 2% thin can cause problems when it is milled; a relatively uniform kernel size is desirable from this standpoint.<br /><br />From https://www.probrewer.com/library/malt/understanding-malt-analysis-sheets/:<br /><br />European malts often list only the percentage of malt that can be sieved through 2.2 mm openings. Brewers will reject a malt if it’s more than 1% thin or 2% less than 2.2 mm, because these values indicate unmodified kernels.  Other analyses are given in terms of screen separation and brewers will typically see percentages of kernels that will remain on a screen with 5/64 inch, 6/64 inch, and 7/64 inch openings.  Kernels considered thin will fall through the 5/64-in. opening. Generally speaking, the plumper the malt kernels, the better the yield.  The uniformity of malt sizes measures how uniformly the malt will crush. Any lot of malt that will crush reasonably well must have kernels that are at least 90% adjacent sizes, regardless of the plumpness. |
| half |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage of malt that is "half glassy".  For a malt, % "glassy" + % "half glassy" + % "mealy" = 100%. |
| mealy |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage of malt that is "mealy".  For a malt, % "glassy" + % "half glassy" + % "mealy" = 100%.<br /><br />(The opposite of mealiness is “vitreosity,” which is sometimes used as an alternative measurement.  A value of 1 is assigned to glassy (vitreous) kernels, 0.5 to half-glassy and 0 to mealy kernels. The percentages of each are summed and averaged; a vitreosity value of 0.25 or less is considered desirable.) |
| thru |  | [Measurement::Percentage](./Measurement.md#percentage) | The Percentage of grain that makes it through a thin mesh screen, typically 5/64 inch. Values less than 3% are desired. |
| friability |  | [Measurement::Percentage](./Measurement.md#percentage) | Friability is the measure of a malts ability to crumble during the crush, and is used as an indicator for easy gelatinization of the grain and starches, as well as modification of the malt. Value of 85% of higher indicates a well modified malt and is suitable for single step mashes. Lower values may require a step mash. |
| di_pH |  | [Measurement::Acidity](./Measurement.md#acidity) | The pH of the resultant wort for 1 lb of grain mashed in 1 gallon of distilled water. Used in many water chemistry / mash pH prediction software. |
| viscosity |  | [Measurement::Viscosity](./Measurement.md#viscosity) | The measure of wort viscosity, typically associated with the breakdown of beta-glucans. The higher the viscosity, the greater the need for a glucan rest and the less suitable for a fly sparge. |
| dms_p |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | The amount of DMS precursors, namely S-methyl methionine (SMM) and dimethyl sulfoxide (DMSO) in the malt which convert to dimethyl sulfide (DMS). |
| fan |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Free Amino Nitrogen (FAN) is a critical yeast nutrient. Typical values for base malt is 170. |
| fermentability |  | [Measurement::Percentage](./Measurement.md#percentage) | Fermentability - Used in Extracts to indicate a baseline typical apparent attenuation for a typical medium attenuation yeast. |
| beta_glucan |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Values of 180 or more may suggest a glucan rest and avoiding fly sparging. |


---

# Component Types

## FermentableBase

FermentableBase provides unique properties to identify individual records of fermentable ingredients.

<strong>FermentableBase</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| type | ✅ | Enum:<br>&nbsp;∙ `dry extract`<br>&nbsp;∙ `extract`<br>&nbsp;∙ `grain`<br>&nbsp;∙ `sugar`<br>&nbsp;∙ `fruit`<br>&nbsp;∙ `juice`<br>&nbsp;∙ `honey`<br>&nbsp;∙ `other` |  |
| color | ✅ | [Measurement::Color](./Measurement.md#color) | Maltsters typically measure grain color in degrees Lovibond, but other units are supported here. |
| origin |  | string | Country or place of origin |
| producer |  | string |  |
| product_id |  | string |  |
| grain_group |  | Enum:<br>&nbsp;∙ `base`<br>&nbsp;∙ `caramel`<br>&nbsp;∙ `flaked`<br>&nbsp;∙ `roasted`<br>&nbsp;∙ `specialty`<br>&nbsp;∙ `smoked`<br>&nbsp;∙ `adjunct` | This should only be set when `type` is `grain`. |
| yield_fine_grind |  | [Measurement::Percentage](./Measurement.md#percentage) | Extract Yield Dry Basis Fine Grind (DBFG) - aka percentage yield, compared to sucrose, of a fine grind. |
| yield_coarse_grind |  | [Measurement::Percentage](./Measurement.md#percentage) | Extract Yield Dry Basis Coarse Grind (DBCG) - aka percentage yield, compared to sucrose, of a coarse grind. |
| yield_fine_coarse_difference |  | [Measurement::Percentage](./Measurement.md#percentage) | Extract Fine Grind/Coarse Grind Difference (FG/CG) - aka the difference in yield between coarsely milled and finely milled grain.  A FG/CG difference of 0.5–1.0 percentage points is well suited to a single step infusion, while a value greater than 1.5 percentage points indicates that a protein rest or step mash may be advisable.<br />Note that `fine_coarse_difference` should be the same as `fine_grind` minus `coarse_grind`. |
| yield_potential |  | [Measurement::Density](./Measurement.md#density) | The potential yield is the specific gravity that can be achieved with 1.00 pound (455 g) of malt mashed in 1.00 gallon (3.78 L) of water.  Calculated as (extract) potential (SG) = 1 + (DBFG / 100) * 0.04621. |

## FermentableInventory



<strong>FermentableInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| amount |  | [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-06-10 at 09:03:35+0200.
