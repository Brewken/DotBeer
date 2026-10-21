# Misc

Miscellaneous ingredients that are not hops, fermentables, yeasts/cultures or water.  Some people would call these "non-fermentable adjuncts", but there are also narrower definitions of "adjunct", so we do not use that term.  Also often referred to as "other ingredients", but we already use "other" in a lot of classifications, so we prefer "miscellaneous" as abbreviated to "misc".

<strong>Misc</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| misc_type | ✅ | Enum:<br>&nbsp;∙ `spice`<br>&nbsp;∙ `fining`<br>&nbsp;∙ `water agent`<br>&nbsp;∙ `herb`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `wood`<br>&nbsp;∙ `other` | If this is `water agent` then `water_agent_type` should also be set. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this Misc object. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Misc object. |
| producer |  | string |  |
| product_id |  | string | Producer’s product code or number for this item. |
| water_agent_type |  | Enum:<br>&nbsp;∙ `calcium chloride anhydrous`<br>&nbsp;∙ `calcium chloride dihydrate`<br>&nbsp;∙ `calcium carbonate`<br>&nbsp;∙ `calcium sulfate dihydrate`<br>&nbsp;∙ `calcium hydroxide`<br>&nbsp;∙ `magnesium sulfate heptahydrate`<br>&nbsp;∙ `magnesium chloride hexahydrate`<br>&nbsp;∙ `sodium chloride`<br>&nbsp;∙ `sodium bicarbonate`<br>&nbsp;∙ `lactic acid`<br>&nbsp;∙ `phosphoric acid`<br>&nbsp;∙ `sulfuric acid`<br>&nbsp;∙ `hydrochloric acid`<br>&nbsp;∙ `other` | Must be set if and only if `misc_type` is `water agent`.<br>`calcium chloride anhydrous` = CaCl₂<br>`calcium chloride dihydrate` = CaCl₂·2H₂O (Usual food-grade “flake”)<br>`calcium carbonate` = CaCO₃ (anhydrous; eg chalk)<br>`calcium sulfate dihydrate` = CaSO₄·2H₂O (gypsum)<br>`calcium hydroxide` = Ca(OH)₂ (pickling lime)<br>`magnesium sulfate heptahydrate` = MgSO₄·7H₂O  aka Epsom salt<br>`magnesium chloride hexahydrate` = MgCl₂·6H₂O<br>`sodium chloride` = NaCl  aka "regular" salt<br>`sodium bicarbonate` = NaHCO₃<br>`lactic acid` = CH₃CH(OH)CO₂H (extended formula) = C₃H₆O₃ (regular formula)<br>`phosphoric acid` = H₃PO₄<br>`sulfuric acid` = H₂SO₄<br>`hydrochloric acid` = HCl<br>`other` = none of the above |
| water_agent_percent_acid |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Should only be set if `misc_type` is `water agent` and `water_agent_type` is `lactic acid`, `phosphoric acid` or `other`. |
| use_for |  | string | Used to describe the purpose of the miscellaneous ingredient, e.g. whirlfloc is used for clarity. |
| notes |  | string |  |


---

# Component Types

## MiscAmount

The ways in which an amount of a Misc could be measured



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-21 at 19:47:37+0200.
