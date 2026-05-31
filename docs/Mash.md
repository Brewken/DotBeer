# Mash

A mash procedure, which can be used by multiple recipes.

<strong>Mash</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
name
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
grain_temperature
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Temperature](./Measurement.md#temperature)
</td><td style="border: 1px solid black; padding: 6px;">
Initial grain temperature prior to the start of the mash.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
mash_steps
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[MashStep](#mashstep)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
notes
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>


---

# Definitions

## MashStep

Individual step of a mash.

<strong>MashStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithRampTime](./StepCommon.md#stepwithramptime) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
step_type
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `infusion`<br>&nbsp;∙ `temperature`<br>&nbsp;∙ `decoction`<br>&nbsp;∙ `souring mash`<br>&nbsp;∙ `souring wort`<br>&nbsp;∙ `drain mash tun`<br>&nbsp;∙ `sparge`
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
amount
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Volume](./Measurement.md#volume)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
water_grain_ratio
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::SpecificVolume](./Measurement.md#specificvolume)
</td><td style="border: 1px solid black; padding: 6px;">
Also known as the mash thickness. eg 1.75 qt/lb or 3.65 L/kg.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
infuse_temperature
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Temperature](./Measurement.md#temperature)
</td><td style="border: 1px solid black; padding: 6px;">
Temperature of the water for an infusion step.
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
