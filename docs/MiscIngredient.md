# MiscIngredient

Collects the attributes of an ingredient to store as record information.

<strong>MiscIngredient</strong> is a JSON object with all properties from [MiscIngredientBase](#miscingredientbase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| folder_path |  | string | The suggested slash-delimited subfolder path in which to store this MiscIngredient object.  NB: any leading slash should be ignored.  Eg, if folder_path is "/hum/bug" (or "hum/bug") then importing the object into folder "/foo/bar" should result in its folder path being "/foo/bar/hum/bug".  If the importing software does not support folders, then it should ignore this field. |
| use_for |  | string | Used to describe the purpose of the miscellaneous ingredient, e.g. whirlfloc is used for clarity. |
| notes |  | string |  |
| inventory |  | [MiscIngredientInventory](#miscingredientinventory) |  |


---

# Component Types

## MiscIngredientBase

Miscellaneous ingredients that are not hops, fermentables, yeasts/cultures or water.  Some people would call these "non-fermentable adjuncts", but there are also narrower definitions of "adjunct", so we do not use that term.  Also often referred to as "other ingredients", but we already use "other" in a lot of classifications, so we prefer "miscellaneous" as abbreviated to "misc".

<strong>MiscIngredientBase</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| misc_type | ✅ | Enum:<br>&nbsp;∙ `spice`<br>&nbsp;∙ `fining`<br>&nbsp;∙ `water agent`<br>&nbsp;∙ `herb`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `wood`<br>&nbsp;∙ `other` | If this is `water agent` then `water_agent_type` should also be set. |
| producer |  | string |  |
| product_id |  | string |  |
| water_agent_type |  | Enum:<br>&nbsp;∙ `calcium chloride`<br>&nbsp;∙ `calcium carbonate`<br>&nbsp;∙ `calcium sulfate`<br>&nbsp;∙ `magnesium sulfate`<br>&nbsp;∙ `sodium chloride`<br>&nbsp;∙ `sodium bicarbonate`<br>&nbsp;∙ `lactic acid`<br>&nbsp;∙ `phosphoric acid`<br>&nbsp;∙ `other` | Should only be set if `misc_type` is `water agent`.<br>`calcium chloride` = CaCl₂<br>`calcium carbonate` = CaCO₃<br>`calcium sulfate` = CaSO₄<br>`magnesium sulfate` = MgSO₄<br>`sodium chloride` = NaCl  aka "regular" salt<br>`sodium bicarbonate` = NaHCO₃<br>`lactic acid` = CH₃CH(OH)CO₂H (extended formula) = C₃H₆O₃ (regular formula)<br>`phosphoric acid` = H₃PO₄<br>`other` = none of the above |
| water_agent_percent_acid |  | [Measurement::Percentage](./Measurement.md#percentage) | Should only be set if `misc_type` is `water agent`. |

## MiscIngredientInventory



<strong>MiscIngredientInventory</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| amount | ✅ | [Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.4.0) on 2026-08-08 at 19:08:56+0200.
