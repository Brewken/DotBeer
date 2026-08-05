# StepCommon

`StepCommon` is not a type itself, but a subschema holding various common parts of `MashStep`, `BoilStep` and `FermentationStep`.


---

# Component Types

## StepBase

Common attributes of MashStep, BoilStep and FermentationStep.

<strong>StepBase</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| step_description |  | string |  |
| step_time |  | [Measurement::Time](./Measurement.md#time) |  |
| start_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | For a MashStep this is also known as the step temperature, and is the target temperature for this step |
| end_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) |  |
| start_pH |  | [Measurement::Acidity](./Measurement.md#acidity) |  |
| end_pH |  | [Measurement::Acidity](./Measurement.md#acidity) |  |

## StepWithRampTime

Common attribute of MashStep and BoilStep but not FermentationStep.

<strong>StepWithRampTime</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| ramp_time |  | [Measurement::Time](./Measurement.md#time) | The amount of time that passes before this step begins. eg moving from a mash step (step 1) of 148°F, to a new temperature step of 156°F (step 2) may take 8 minutes to heat the mash. Step 2 would have a ramp time of 8 minutes. |

## StepWithGravity

Common attributes of BoilStep and FermentationStep but not MashStep.

<strong>StepWithGravity</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| start_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) |
| end_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.3.0) on 2026-08-05 at 09:03:16+0200.
