# Boil

A boil procedure, which can be used by multiple recipes.  A boil procedure with no steps is the same as a standard single step boil.

<strong>Boil</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| boil_time | ✅ | [Measurement::Time](./Measurement.md#time) |
| name |  | string |
| boil_description |  | string |
| notes |  | string |
| pre_boil_size |  | [Measurement::Volume](./Measurement.md#volume) |
| boil_steps |  | [BoilStep](#boilstep) |


---

# Definitions

## BoilStep

Individual step of a boil, including preboil steps, non-boiling pasteurization steps, boiling, whirlpool steps, and chilling.

<strong>BoilStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase), [StepCommon::StepWithRampTime](./StepCommon.md#stepwithramptime) and [StepCommon::StepWithGravity](./StepCommon.md#stepwithgravity) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| chilling_type |  | Enum:<br>&nbsp;∙ `batch`<br>&nbsp;∙ `inline` | Chilling type separates batch chilling, eg immersion chillers, where the entire volume of wort is brought down in temperature as a whole, vs inline chilling where the wort is chilled while it is being drained, which can leave a significant amount of hop isomerization occurring in the boil kettle. |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
