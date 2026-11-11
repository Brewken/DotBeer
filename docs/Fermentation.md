# Fermentation

A fermentation procedure, which can be used by multiple recipes.

<strong>Fermentation</strong> is a JSON object with the following properties:

| Property | Required? | Type | Since | Description |
| -------- | --------- | ---- | ----- | ----------- |
| name | ✅ | string |  |  |
| fermentation_steps | ✅ | array of [FermentationStep](#fermentationstep) |  | The steps that make up the fermentation, in the order they are performed. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) |  | The "local ID" that allows other objects in this file (eg recipes) to refer to this fermentation. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) |  | The suggested slash-delimited subfolder path in which to store this Fermentation object. |
| locked |  | boolean | 1.1.0 | If `true`, this fermentation has been marked as one that should not be changed -- eg a standard fermentation profile used by many recipes.  Software that supports locking should not allow a locked fermentation to be changed or deleted unless the user first explicitly unlocks it.  It should, however, allow a locked fermentation to be used in recipes and to be copied (with the copy not being locked).  Software that does not support locking can ignore this field.  If the field is absent, the fermentation is not locked. |
| fermentation_description |  | string |  |  |
| notes |  | string |  |  |
| krausen_handling |  | Enum:<br>&nbsp;∙ `mixed in`<br>&nbsp;∙ `minor deposits`<br>&nbsp;∙ `medium deposits`<br>&nbsp;∙ `heavy deposits`<br>&nbsp;∙ `very heavy deposits`<br>&nbsp;∙ `blown off, slow fermentation`<br>&nbsp;∙ `blown off, normal fermentation`<br>&nbsp;∙ `blown off, vigorous fermentation` | 1.1.0 | What happens to the krausen (the foam on top of the fermenting beer), which carries away some bitterness compounds:<ul><li>`mixed in`: the krausen is mixed back into the beer (or is suppressed, eg with anti-foam), so nothing is lost</li><li>`minor deposits`, `medium deposits`, `heavy deposits`, `very heavy deposits`: some of the krausen is left stuck to the walls of the fermenter above the beer</li><li>`blown off, slow fermentation`, `blown off, normal fermentation`, `blown off, vigorous fermentation`: the krausen is lost through a blow-off tube, with more being lost the more vigorous the fermentation</li></ul>(This is used, eg, by the SMPH model of IBUs.)  If absent, `medium deposits` is assumed.  Skimming the krausen can be recorded as one of the `blown off` values, according to how much is removed. |


---

# Component Types

## FermentationStep

Individual step of a fermentation.

<strong>FermentationStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithGravity](./StepCommon.md#stepwithgravity) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| free_rise |  | boolean | Free rise is used to indicate a fermentation step where the exothermic fermentation is allowed to raise the temperature without restriction. |
| vessel |  | string | Name of the vessel the step takes place in, which is how a transfer between vessels is recorded. |
| vessel_pressure |  | [Measurement::Pressure](./Measurement.md#pressure) | The (gauge) pressure at which the fermentation vessel is held during this step, eg by a spunding valve or a regulator -- ie the pressure that the CO₂ produced by fermentation is allowed to build up to, but not beyond.  Typical values for fermenting under pressure are around 0.5–1 bar (7–15 psi).  If this field is absent, the step is not under pressure (ie the vessel is vented to the atmosphere, eg via an airlock), or the pressure is not known.<br /><br />A change of pressure part way through fermentation (eg closing a spunding valve towards the end of fermentation to naturally carbonate the beer) is recorded by starting a new step. |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.1.0) on 2026-11-11 at 09:28:54+0100.
