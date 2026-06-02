# MiscIngredient

Collects the attributes of an ingredient to store as record information.

<strong>MiscIngredient</strong> is a JSON object with all properties from [MiscIngredientBase](#miscingredientbase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| use_for |  | string | Used to describe the purpose of the miscellaneous ingredient, e.g. whirlfloc is used for clarity. |
| notes |  | string |  |
| inventory |  | [MiscIngredientInventory](#miscingredientinventory) |  |


---

# Definitions

## MiscIngredientBase

Miscellaneous ingredients that are not hops, fermentables, yeasts/cultures or water.  Some people would call these "non-fermentable adjuncts", but there are also narrower definitions of "adjunct", so we do not use that term.  Also often referred to as "other ingredients", but we already use "other" in a lot of classifications, so we prefer "miscellaneous" as abbreviated to "misc".

<strong>MiscIngredientBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| name | ✅ | string |
| producer |  | string |
| product_id |  | string |
| misc_type |  | Enum:<br>&nbsp;∙ `spice`<br>&nbsp;∙ `fining`<br>&nbsp;∙ `water agent`<br>&nbsp;∙ `herb`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `wood`<br>&nbsp;∙ `other` |

## MiscIngredientInventory



<strong>MiscIngredientInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| amount | ✅ | [Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |



---

<footer>
Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-06-02 at 15:20:29+0200.
</footer>
