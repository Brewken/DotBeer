# Mash

A mash procedure, which can be used by multiple recipes.

<strong>Mash</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| grain_temperature | ✅ | [Measurement::Temperature](./Measurement.md#temperature) | Initial grain temperature prior to the start of the mash. |
| mash_steps | ✅ | array of [MashStep](#mashstep) | The steps that make up the mash, in the order they are performed. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this mash. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Mash object. |
| notes |  | string |  |


---

# Component Types

## MashStep

A mash step is an internal record used within a mash profile to denote a separate step in a multi-step mash.  A mash step is not intended for use outside of a mash profile.

<strong>MashStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithRampTime](./StepCommon.md#stepwithramptime) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| step_type | ✅ | Enum:<br>&nbsp;∙ `infusion`<br>&nbsp;∙ `temperature`<br>&nbsp;∙ `decoction`<br>&nbsp;∙ `souring mash`<br>&nbsp;∙ `souring wort`<br>&nbsp;∙ `drain mash tun`<br>&nbsp;∙ `sparge` | `infusion` = raise or set the mash temperature by adding hot water (`amount` is the volume added, and `infuse_temperature` its temperature)<br>`temperature` = raise or hold the mash temperature by applying heat directly (eg a heated or recirculating mash tun), without adding water<br>`decoction` = raise the mash temperature by drawing off part of the mash, boiling it and returning it (`amount` is the volume drawn off)<br>`souring mash` = hold the mash, grain included, warm with lactic acid bacteria (whether added or naturally present on the grain) to sour it before lautering (aka sour mashing)<br>`souring wort` = hold the separated wort, without grain, warm with lactic acid bacteria to sour it before the boil (aka kettle souring)<br>`drain mash tun` = run the wort off from the mash tun into the kettle, eg collecting the first runnings, or between batch sparges<br>`sparge` = rinse the grain bed with hot water to extract remaining sugars, either continuously (fly sparge) or in batches (batch sparge) |
| amount |  | [Measurement::Volume](./Measurement.md#volume) | For an `infusion` step, this is the volume of water to infuse in this step.  For a `decoction` step, this is the calculated volume of mash drawn off to be boiled and returned to the main mash (typically calculated from the target temperature rise).  For a `sparge` step, this is the volume of water added.<br /><br />This field is normally only meaningful when `step_type` is `infusion`, `decoction` or `sparge`. |
| water_grain_ratio |  | [Measurement::VolumePerMass](./Measurement.md#volumepermass) | Also known as the mash thickness, this is total ratio of water to grain (eg 1.75 qt/lb or 3.65 l/kg) for this step AFTER the infusion.  Note this value must be consistent with the required infusion amount and amounts added in earlier steps.<br /><br />This field is normally only meaningful when `step_type` is `infusion`. |
| infuse_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Temperature of the water for an infusion step -- typically calculated based on the current step, grain, and other settings.<br /><br />This field is normally only meaningful when `step_type` is `infusion`. |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-23 at 12:55:01+0200.
