# Hop

Full definition of a hop variety.

<strong>Hop</strong> is a JSON object with all properties from [HopBase](#hopbase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | -------- | --------------- | ----------- |
| type |  | Enum:<br>&nbsp;∙ `aroma`<br>&nbsp;∙ `bittering`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `aroma/bittering`<br>&nbsp;∙ `bittering/flavor`<br>&nbsp;∙ `aroma/flavor`<br>&nbsp;∙ `aroma/bittering/flavor` |  |
| notes |  | string |  |
| six_month_alpha_loss |  | [Measurement::Percentage](./Measurement.md#percentage) | Defined as the percentage of hop alpha lost in 6 months of storage. |
| substitutes |  | string |  |
| oil_content |  | object | Collects all information of a hop variety pertaining to oil content, polyphenols, and thiols. Each individual compound is expressed as a percent of the total oil measurement. |
| oil_content.total_oil_ml_per_100g |  | number | The total amount of oil, including hydrocarbons, esters, and terpene alcohols in units of ml of oil per 100g of hop mass. |
| oil_content.humulene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.caryophyllene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.cohumulone |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.myrcene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.farnesene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.geraniol |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.b_pinene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.linalool |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.limonene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.nerol |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.pinene |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.polyphenols |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| oil_content.xanthohumol |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| inventory |  | [HopInventory](#hopinventory) |  |


---

# Definitions

## HopBase

Minimal properties to identify individual records of a hop variety.

<strong>HopBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | -------- | --------------- |
| name | ✅ | string |
| alpha_acid | ✅ | [Measurement::Percentage](./Measurement.md#percentage) |
| producer |  | string |
| product_id |  | string |
| origin |  | string |
| year |  | string |
| form |  | Enum:<br>&nbsp;∙ `extract`<br>&nbsp;∙ `leaf`<br>&nbsp;∙ `leaf (wet)`<br>&nbsp;∙ `pellet`<br>&nbsp;∙ `powder`<br>&nbsp;∙ `plug` |
| beta_acid |  | [Measurement::Percentage](./Measurement.md#percentage) |

## HopInventory

No description provided for this model.

<strong>HopInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | -------- | --------------- |
| amount |  | [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
