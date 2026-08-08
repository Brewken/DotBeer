# Fermentation

A fermentation procedure, which can be used by multiple recipes.

<strong>Fermentation</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| fermentation_steps | ✅ | array of [FermentationStep](#fermentationstep) |  |
| folder_path |  | string | The suggested slash-delimited subfolder path in which to store this Fermentation object.  NB: any leading slash should be ignored.  Eg, if folder_path is "/hum/bug" (or "hum/bug") then importing the object into folder "/foo/bar" should result in its folder path being "/foo/bar/hum/bug".  If the importing software does not support folders, then it should ignore this field. |
| fermentation_description |  | string |  |
| notes |  | string |  |


---

# Component Types

## FermentationStep

Individual step of a fermentation.

<strong>FermentationStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithGravity](./StepCommon.md#stepwithgravity) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| free_rise |  | boolean | Free rise is used to indicate a fermentation step where the exothermic fermentation is allowed to raise the temperature without restriction This is either True or false. |
| vessel |  | string |  |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.4.0) on 2026-08-08 at 19:08:56+0200.
