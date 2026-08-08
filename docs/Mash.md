# Mash

A mash procedure, which can be used by multiple recipes.

<strong>Mash</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| grain_temperature | ✅ | [Measurement::Temperature](./Measurement.md#temperature) | Initial grain temperature prior to the start of the mash. |
| mash_steps | ✅ | array of [MashStep](#mashstep) |  |
| folder_path |  | string | The suggested slash-delimited subfolder path in which to store this Mash object.  NB: any leading slash should be ignored.  Eg, if folder_path is "/hum/bug" (or "hum/bug") then importing the object into folder "/foo/bar" should result in its folder path being "/foo/bar/hum/bug".  If the importing software does not support folders, then it should ignore this field. |
| notes |  | string |  |


---

# Component Types

## MashStep

A mash step is an internal record used within a mash profile to denote a separate step in a multi-step mash.  A mash step is not intended for use outside of a mash profile.

<strong>MashStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithRampTime](./StepCommon.md#stepwithramptime) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| step_type | ✅ | Enum:<br>&nbsp;∙ `infusion`<br>&nbsp;∙ `temperature`<br>&nbsp;∙ `decoction`<br>&nbsp;∙ `souring mash`<br>&nbsp;∙ `souring wort`<br>&nbsp;∙ `drain mash tun`<br>&nbsp;∙ `sparge` | Infusion denotes adding hot water, temperature denotes heating with an outside heat source, and decoction denotes drawing off some mash for boiling. |
| amount |  | [Measurement::Volume](./Measurement.md#volume) | For a infusion step, this is the volume of water to infuse in this step.  For a decoction step, this is the calculated volume of mash to decoction. |
| water_grain_ratio |  | [Measurement::SpecificVolume](./Measurement.md#specificvolume) | Also known as the mash thickness. eg 1.75 qt/lb or 3.65 L/kg. |
| infuse_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Temperature of the water for an infusion step -- typically calculated based on the current step, grain, and other settings.  Applicable only for an infusion step. |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.4.0) on 2026-08-08 at 19:08:56+0200.
