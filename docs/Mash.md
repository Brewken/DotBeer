# Mash

A mash procedure, which can be used by multiple recipes.

<strong>Mash</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| grain_temperature | ✅ | [Measurement::Temperature](./Measurement.md#temperature) | Initial grain temperature prior to the start of the mash. |
| mash_steps | ✅ | [MashStep](#mashstep) |  |
| notes |  | string |  |


---

# Definitions

## MashStep

Individual step of a mash.

<strong>MashStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithRampTime](./StepCommon.md#stepwithramptime) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| step_type | ✅ | Enum:<br>&nbsp;∙ `infusion`<br>&nbsp;∙ `temperature`<br>&nbsp;∙ `decoction`<br>&nbsp;∙ `souring mash`<br>&nbsp;∙ `souring wort`<br>&nbsp;∙ `drain mash tun`<br>&nbsp;∙ `sparge` |  |
| amount |  | [Measurement::Volume](./Measurement.md#volume) |  |
| water_grain_ratio |  | [Measurement::SpecificVolume](./Measurement.md#specificvolume) | Also known as the mash thickness. eg 1.75 qt/lb or 3.65 L/kg. |
| infuse_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Temperature of the water for an infusion step. |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
