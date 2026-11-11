# Boil

A boil procedure, which can be used by multiple recipes.  Unlike in BeerJSON, a boil must have at least one step: a standard single step boil is simply a boil with one step.  (There is therefore no separate `boil_time` field, as the length of the boil comes from its steps.)

<strong>Boil</strong> is a JSON object with the following properties:

| Property | Required? | Type | Since | Description |
| -------- | --------- | ---- | ----- | ----------- |
| name | ✅ | string |  |  |
| boil_steps | ✅ | array of [BoilStep](#boilstep) |  | The steps that make up the boil, in the order they are performed. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) |  | The "local ID" that allows other objects in this file (eg recipes) to refer to this boil. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) |  | The suggested slash-delimited subfolder path in which to store this Boil object. |
| locked |  | boolean | 1.1.0 | If `true`, this boil has been marked as one that should not be changed -- eg a standard boil profile used by many recipes.  Software that supports locking should not allow a locked boil to be changed or deleted unless the user first explicitly unlocks it.  It should, however, allow a locked boil to be used in recipes and to be copied (with the copy not being locked).  Software that does not support locking can ignore this field.  If the field is absent, the boil is not locked. |
| boil_description |  | string |  |  |
| notes |  | string |  |  |
| pre_boil_size |  | [Measurement::Volume](./Measurement.md#volume) |  | Volume of wort at the start of the boil. |


---

# Component Types

## BoilStep

Individual step of a boil, including preboil steps, non-boiling pasteurization steps, boiling, whirlpool steps, and chilling.

If `start_temperature` or `end_temperature` is not given, the step is assumed to be at boiling at that point.  Steps are classified as pre-boil, boil proper or post-boil by their temperatures (see `AdditionSchedule` in [Recipe](./Recipe.md#additionschedule) for details).

<strong>BoilStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase), [StepCommon::StepWithRampTime](./StepCommon.md#stepwithramptime) and [StepCommon::StepWithGravity](./StepCommon.md#stepwithgravity) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| chilling_type |  | Enum:<br>&nbsp;∙ `batch`<br>&nbsp;∙ `inline` | Chilling type separates batch chilling, eg immersion chillers, where the entire volume of wort is brought down in temperature as a whole, vs inline chilling where the wort is chilled while it is being drained, which can leave a significant amount of hop isomerization occurring in the boil kettle. |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.1.0) on 2026-11-11 at 09:14:02+0100.
