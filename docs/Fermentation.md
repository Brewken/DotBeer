# Fermentation

A fermentation procedure, which can be used by multiple recipes.

<strong>Fermentation</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| fermentation_steps | ✅ | array of [FermentationStep](#fermentationstep) | The steps that make up the fermentation, in the order they are performed. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this fermentation. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Fermentation object. |
| fermentation_description |  | string |  |
| notes |  | string |  |


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

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.0.0) on 2026-10-30 at 08:15:20+0100.
