# Water

Full definition of a water profile.

<strong>Water</strong> is a JSON object with all properties from [WaterBase](#waterbase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| folder_path |  | string | The suggested slash-delimited subfolder path in which to store this Water object.  NB: any leading slash should be ignored.  Eg, if folder_path is "/hum/bug" (or "hum/bug") then importing the object into folder "/foo/bar" should result in its folder path being "/foo/bar/hum/bug".  If the importing software does not support folders, then it should ignore this field. |
| pH |  | [Measurement::Acidity](./Measurement.md#acidity) | Acidity of the water profile |
| notes |  | string |  |


---

# Component Types

## MineralIonConcentrations

Concentrations of various mineral ions of interest to brewers.

<strong>MineralIonConcentrations</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| bicarbonate | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Bicarbonate (HCO₃⁻) content of the water profile |
| calcium | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Calcium (Ca²⁺) content of the water profile.  Calcium is by far the most influential mineral in the brewing process.  It is instrumental to many yeast, enzyme, and protein reactions, both in the mash and in the boil.  Yeast flocculation is improved by calcium; most yeast strains require at least 50 mg/L Ca²⁺ ions for good flocculation.  Calcium reacts with phosphates, forming precipitates that involve the release of hydrogen ions, in turn lowering the pH of the mash. |
| chloride | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Chloride (Cl⁻) content of the water profile.  Common in most water supplies, chloride ions contribute to the mellow, palate-full character of a beer. |
| magnesium | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Magnesium (Mg²⁺) content of the water profile.  Magnesium ions react similarly to calcium ions and malt phytins, but since magnesium salts are much more soluble, the effect on wort pH is not as great.  Magnesium is most important for its benefit to yeast metabolism during fermentation. |
| sodium | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Sodium (Na⁺) content of the water profile.  Although it has no chemical effect, sodium contributes to the perceived flavor of beer.  Levels from 75 to 150 mg/L give a round smoothness and accentuate sweetness, which is most pleasant when paired with chloride ions than when associated with sulfate ions.  In the presence of sulfate, sodium creates an unpleasant harshness, so the rule of thumb is that the more sulfate in the water, the less sodium there should be (and vice versa). |
| sulfate | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Sulfate (SO₄²⁻) content of the water profile.  Sulfates positively affect protein and starch degradation, which favors mash filtration and trub sedimentation.  However, if levels are too high, it can cause poor hop utilization (bitterness will not easily be extracted).  In moderation, sulfates can lend a dry, crisp palate to the finished beer.  If used in excess, the finished beer will have a harsh, salty, and laxative character. |
| carbonate |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Carbonate (CO₃²⁻) content of the water profile.  Carbonate raises pH and can result in less fermentable worts (a higher dextrin/maltose ratio), unacceptable wort color values, difficulties in wort filtration, and less efficient separation of protein and protein-tannin elements during the hot and cold breaks.  High carbonate waters can affect hop flavor too: hop bitterness becomes increasingly harsher. |
| copper |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Copper (Cu²⁺) content of the water profile.  In concentrations as low as 0.1 mg/L, copper ions can act as catalysts of oxidants, leading to irreversible beer haze. |
| fluoride |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Fluoride (F⁻) content of the water profile |
| iron |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Iron (Fe²⁺) content of the water profile.  In large amounts, iron can contribute negative flavor characters (eg metallic and astringent) to beer. |
| manganese |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Manganese (Mn²⁺) content of the water profile.  Manganese is important for proper enzyme action and has a positive action on protein solubilization and yeast. |
| nitrate |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Nitrate (NO₃⁻) content of the water profile.  Nitrate in and of itself, is not a problem; it has no effect on beer flavor or brewing reactions. |
| nitrite |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Nitrite (NO₂⁻) content of the water profile.  High nitrite levels may reduce the fermentation rate, dampen the rate of pH reduction, and give rise to higher levels of vicinal diketones. |
| phosphate |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Phosphate (PO₄³⁻) content of the water profile.  Phosphate compounds are important pH buffers in brewing and useful for reducing the pH in mashing and during the boil.  There are usually regulatory limits on the concentration of phosphates in potable water.  Most of the phosphate in beer is derived from malt, although phosphoric acid or acid phosphate salts may be used to adjust the pH or to release carbon dioxide from bicarbonate-rich waters. |
| potassium |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Potassium (K⁺) content of the water profile.  Like sodium, potassium can create a “salty” flavor effect.  It is required for yeast growth and inhibits certain mash enzymes at concentrations above 10 mg/L. |
| zinc |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) | Zinc (Zn²⁺) content of the water profile.  Zinc plays an important role in fermentation and has a positive action on protein synthesis and yeast growth.  It also affects flocculation and stabilizes foam (promoting lacing). |

## WaterBase

Provides unique properties to identify individual records of brewing water.  NOTE that water is handled differently from other ingredients.  We don't model inventory of water, it doesn't have producers or product IDs, and the amounts needed in a recipe are already defined in its mash steps rather than by RecipeAddition amounts.

<strong>WaterBase</strong> is a JSON object with all properties from [MineralIonConcentrations](#mineralionconcentrations) as well as these additional ones:

| Property | Required? | Type |
| -------- | --------- | ---- |
| name |  | string |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.4.0) on 2026-08-08 at 19:08:56+0200.
