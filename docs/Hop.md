# Hop

Full definition of a hop variety.

<strong>Hop</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| alpha_acid | ✅ | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The actual alpha acid content of the specific year's harvest (and batch) of this type of hop. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this hop. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Hop object. |
| producer |  | string |  |
| product_id |  | string |  |
| origin |  | string | Country of origin for the hop variety |
| year |  | string | Year of harvest.  (Note that this is intentionally not a number, as, for one thing, years are not generally formatted in the same way as numbers.) |
| form |  | Enum:<br>&nbsp;∙ `extract`<br>&nbsp;∙ `leaf`<br>&nbsp;∙ `leaf (wet)`<br>&nbsp;∙ `pellet`<br>&nbsp;∙ `powder`<br>&nbsp;∙ `plug` |  |
| alpha_acid_range |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) | The typical range of alpha acid for this type of hop. |
| beta_acid |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The actual beta acid content of the specific year's harvest (and batch) of this type of hop. |
| beta_acid_range |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) | The typical range of beta acid for this type of hop. |
| hop_type |  | Enum:<br>&nbsp;∙ `aroma`<br>&nbsp;∙ `bittering`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `aroma/bittering`<br>&nbsp;∙ `bittering/flavor`<br>&nbsp;∙ `aroma/flavor`<br>&nbsp;∙ `aroma/bittering/flavor` |  |
| notes |  | string |  |
| six_month_alpha_loss |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The percentage of hop alpha lost in 6 months of storage.<br /><br />Note that this is percentage and not percentage points.  So, eg, if a hop starts out with 4.0% `alpha_acid` and has 25% `six_month_alpha_loss`, then we would expect its alpha acid to be 3.0% after six months in storage. |
| substitutes |  | string | Alternate hop varieties that can be used in place of this hop variety |
| oil_content |  | [OilContent](#oilcontent) |  |
| inventory |  | [HopAmount](#hopamount) |  |


---

# Component Types

## HopAmount

The ways in which an amount of a Hop could be measured

## OilContent

Collects all information of a hop variety pertaining to oil content, polyphenols, and thiols. Each individual compound is expressed as a percent of the total oil measurement.

<strong>OilContent</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| total_oil_ml_per_100g |  | number | The total amount of oil, including hydrocarbons, esters, and terpene alcohols in units of ml of oil per 100g of hop mass. |
| humulene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| caryophyllene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| cohumulone |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| myrcene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| farnesene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| geraniol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| b_pinene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| linalool |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| limonene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| nerol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| pinene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| polyphenols |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |
| xanthohumol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) |  |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (vNone) on 2026-10-07 at 21:10:48+0200.
