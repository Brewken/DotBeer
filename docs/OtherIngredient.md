# OtherIngredient

Collects the attributes of an ingredient to store as record information.

<strong>OtherIngredient</strong> is a JSON object with all properties from [OtherIngredientBase](#otheringredientbase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| use_for |  | string | Used to describe the purpose of the miscellaneous ingredient, e.g. whirlfloc is used for clarity. |
| notes |  | string |  |
| inventory |  | [OtherIngredientInventory](#otheringredientinventory) |  |


---

# Definitions

## OtherIngredientBase

Ingredients that are not hops, fermentables, yeasts/cultures or water.  Some people would call these "other ingredients" "non-fermentable adjuncts", but there are also narrower definitions of "adjunct", so we do not use that term.

<strong>OtherIngredientBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| name | ✅ | string |
| type | ✅ | Enum:<br>&nbsp;∙ `spice`<br>&nbsp;∙ `fining`<br>&nbsp;∙ `water agent`<br>&nbsp;∙ `herb`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `wood`<br>&nbsp;∙ `other` |
| producer |  | string |
| product_id |  | string |

## OtherIngredientInventory

No description provided for this model.

<strong>OtherIngredientInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| amount | ✅ | [Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
