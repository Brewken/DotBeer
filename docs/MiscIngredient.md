# MiscIngredient

Miscellaneous ingredients that are not hops, fermentables, yeasts/cultures or water.  Some people would call these "non-fermentable adjuncts", but there are also narrower definitions of "adjunct", so we do not use that term.  Also often referred to as "other ingredients", but we already use "other" in a lot of classifications, so we prefer "miscellaneous" as abbreviated to "misc".

<strong>MiscIngredient</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| misc_type | ✅ | Enum:<br>&nbsp;∙ `spice`<br>&nbsp;∙ `fining`<br>&nbsp;∙ `water agent`<br>&nbsp;∙ `herb`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `wood`<br>&nbsp;∙ `other` | If this is `water agent` then `water_agent_type` should also be set. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this MiscIngredient object. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this MiscIngredient object. |
| producer |  | string |  |
| product_id |  | string |  |
| water_agent_type |  | Enum:<br>&nbsp;∙ `calcium chloride`<br>&nbsp;∙ `calcium carbonate`<br>&nbsp;∙ `calcium sulfate`<br>&nbsp;∙ `magnesium sulfate`<br>&nbsp;∙ `sodium chloride`<br>&nbsp;∙ `sodium bicarbonate`<br>&nbsp;∙ `lactic acid`<br>&nbsp;∙ `phosphoric acid`<br>&nbsp;∙ `other` | Should only be set if `misc_type` is `water agent`.<br>`calcium chloride` = CaCl₂<br>`calcium carbonate` = CaCO₃<br>`calcium sulfate` = CaSO₄<br>`magnesium sulfate` = MgSO₄<br>`sodium chloride` = NaCl  aka "regular" salt<br>`sodium bicarbonate` = NaHCO₃<br>`lactic acid` = CH₃CH(OH)CO₂H (extended formula) = C₃H₆O₃ (regular formula)<br>`phosphoric acid` = H₃PO₄<br>`other` = none of the above |
| water_agent_percent_acid |  | [Measurement::Percentage](./Measurement.md#percentage) | Should only be set if `misc_type` is `water agent`. |
| use_for |  | string | Used to describe the purpose of the miscellaneous ingredient, e.g. whirlfloc is used for clarity. |
| notes |  | string |  |
| inventory |  | [MiscIngredientAmount](#miscingredientamount) |  |


---

# Component Types

## MiscIngredientAmount

The ways in which an amount of a MiscIngredient could be measured



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.6.0) on 2026-09-28 at 18:13:30+0200.
