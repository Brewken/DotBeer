# Water

Full definition of a water profile.

<strong>Water</strong> is a JSON object with all properties from [WaterBase](#waterbase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">pH</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Acidity](./Measurement.md#acidity)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">notes</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>


---

# Definitions

## WaterBase

Provides unique properties to identify individual records of brewing water.  NOTE that water is handled differently from other ingredients.  We don't model inventory of water, it doesn't have producers or product IDs, and the amounts needed in a recipe are already defined in its mash steps rather than by RecipeAddition amounts.

<strong>WaterBase</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">name</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">calcium</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">bicarbonate</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">sulfate</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">chloride</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">sodium</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">magnesium</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">carbonate</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">potassium</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">iron</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">nitrate</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">nitrite</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">fluoride</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](./Measurement.md#massfractionorconcentration)</td>
</tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
