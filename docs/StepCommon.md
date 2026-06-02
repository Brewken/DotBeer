# StepCommon

JSON Schema missing a description, provide it using the `description` key in the root of the JSON document.

<strong>Type:</strong> `object(?)`


---

# Definitions

## StepBase

Common attributes of MashStep, BoilStep and FermentationStep.

<strong>StepBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| name | ✅ | string |
| step_description |  | string |
| step_time |  | [Measurement::Time](./Measurement.md#time) |
| start_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) |
| end_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) |
| start_pH |  | [Measurement::Acidity](./Measurement.md#acidity) |
| end_pH |  | [Measurement::Acidity](./Measurement.md#acidity) |

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
| start_gravity |  | [Measurement::Density](./Measurement.md#density) |
| end_gravity |  | [Measurement::Density](./Measurement.md#density) |



---

<footer>
Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-06-02 at 15:20:29+0200.
</footer>
