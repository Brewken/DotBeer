# Water

Full definition of a water profile.

<strong>Water</strong> is a JSON object with all properties from [WaterBase](#waterbase) as well as these additional ones:

| Property | Required? | Type |
| -------- | --------- | ---- |
| pH |  | [Measurement::Acidity](./Measurement.md#acidity) |
| notes |  | string |


---

# Definitions

## WaterBase

Provides unique properties to identify individual records of brewing water.  NOTE that water is handled differently from other ingredients.  We don't model inventory of water, it doesn't have producers or product IDs, and the amounts needed in a recipe are already defined in its mash steps rather than by RecipeAddition amounts.

<strong>WaterBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| name | ✅ | string |
| calcium | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| bicarbonate | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| sulfate | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| chloride | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| sodium | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| magnesium | ✅ | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| carbonate |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| potassium |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| iron |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| nitrate |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| nitrite |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |
| fluoride |  | [Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31 at 18:49:39+0200.
