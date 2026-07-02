# Hop

Full definition of a hop variety.

<strong>Hop</strong> is a JSON object with all properties from [HopBase](#hopbase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| type |  | Enum:<br>&nbsp;∙ `aroma`<br>&nbsp;∙ `bittering`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `aroma/bittering`<br>&nbsp;∙ `bittering/flavor`<br>&nbsp;∙ `aroma/flavor`<br>&nbsp;∙ `aroma/bittering/flavor` |  |
| notes |  | string |  |
| six_month_alpha_loss |  | [Measurement::Percentage](./Measurement.md#percentage) | Defined as the percentage of hop alpha lost in 6 months of storage. |
| substitutes |  | string | Alternate hop varieties that can be used in place of this hop variety |
| oil_content |  | [OilContent](#oilcontent) |  |
| inventory |  | [HopInventory](#hopinventory) |  |


---

# Component Types

## HopBase

Minimal properties to identify individual records of a hop variety.

<strong>HopBase</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| alpha_acid | ✅ | [Measurement::Percentage](./Measurement.md#percentage) |  |
| producer |  | string |  |
| product_id |  | string |  |
| origin |  | string | Country of origin for the hop variety |
| year |  | string |  |
| form |  | Enum:<br>&nbsp;∙ `extract`<br>&nbsp;∙ `leaf`<br>&nbsp;∙ `leaf (wet)`<br>&nbsp;∙ `pellet`<br>&nbsp;∙ `powder`<br>&nbsp;∙ `plug` |  |
| beta_acid |  | [Measurement::Percentage](./Measurement.md#percentage) |  |

## HopInventory



<strong>HopInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| amount |  | [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |

## OilContent

Collects all information of a hop variety pertaining to oil content, polyphenols, and thiols. Each individual compound is expressed as a percent of the total oil measurement.

<strong>OilContent</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| total_oil_ml_per_100g |  | number | The total amount of oil, including hydrocarbons, esters, and terpene alcohols in units of ml of oil per 100g of hop mass. |
| humulene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| caryophyllene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| cohumulone |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| myrcene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| farnesene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| geraniol |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| b_pinene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| linalool |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| limonene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| nerol |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| pinene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| polyphenols |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| xanthohumol |  | [Measurement::Percentage](./Measurement.md#percentage) |  |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-07-02 at 07:59:16+0200.
