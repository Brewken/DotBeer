# Fermentation

A fermentation procedure, which can be used by multiple recipes.

<strong>Fermentation</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| name | ✅ | string |
| fermentation_steps | ✅ | array of [FermentationStep](#fermentationstep) |
| fermentation_description |  | string |
| notes |  | string |


---

# Definitions

## FermentationStep

Individual step of a fermentation.

<strong>FermentationStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithGravity](./StepCommon.md#stepwithgravity) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| free_rise |  | boolean | Free rise is used to indicate a fermentation step where the exothermic fermentation is allowed to raise the temperature without restriction This is either True or false. |
| vessel |  | string |  |



---

<footer>
Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-06-02 at 15:20:29+0200.
</footer>
