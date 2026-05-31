# Hop

Full definition of a hop variety.

<strong>Hop</strong> is a JSON object with all properties from [HopBase](#hopbase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">type</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">Enum:<br/>&nbsp;∙ `aroma`<br/>
&nbsp;∙ `bittering`<br/>
&nbsp;∙ `flavor`<br/>
&nbsp;∙ `aroma/bittering`<br/>
&nbsp;∙ `bittering/flavor`<br/>
&nbsp;∙ `aroma/flavor`<br/>
&nbsp;∙ `aroma/bittering/flavor`</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">notes</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">six_month_alpha_loss</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">Defined as the percentage of hop alpha lost in 6 months of storage.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">substitutes</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">object</td><td style="border: 1px solid black; padding: 6px;">Collects all information of a hop variety pertaining to oil content, polyphenols, and thiols. Each individual compound is expressed as a percent of the total oil measurement.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.total_oil_ml_per_100g</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">number</td><td style="border: 1px solid black; padding: 6px;">The total amount of oil, including hydrocarbons, esters, and terpene alcohols in units of ml of oil per 100g of hop mass.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.humulene</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.caryophyllene</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.cohumulone</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.myrcene</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.farnesene</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.geraniol</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.b_pinene</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.linalool</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.limonene</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.nerol</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.pinene</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.polyphenols</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">oil_content.xanthohumol</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">inventory</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[HopInventory](#hopinventory)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>


---

# Definitions

## HopBase

Minimal properties to identify individual records of a hop variety.

<strong>HopBase</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">name</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">alpha_acid</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">producer</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">product_id</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">origin</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">year</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">form</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">Enum:<br/>&nbsp;∙ `extract`<br/>
&nbsp;∙ `leaf`<br/>
&nbsp;∙ `leaf (wet)`<br/>
&nbsp;∙ `pellet`<br/>
&nbsp;∙ `powder`<br/>
&nbsp;∙ `plug`</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">beta_acid</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](./Measurement.md#percentage)</td>
</tr>

## HopInventory

No description provided for this model.

<strong>HopInventory</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">amount</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume)</td>
</tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
