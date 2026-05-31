# Boil

A boil procedure, which can be used by multiple recipes.  A boil procedure with no steps is the same as a standard single step boil.

<strong>Boil</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
boil_time
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Time](./Measurement.md#time)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
name
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
boil_description
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
notes
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
pre_boil_size
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Volume](./Measurement.md#volume)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
boil_steps
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[BoilStep](#boilstep)
</td></tr>


---

# Definitions

## BoilStep

Individual step of a boil, including preboil steps, non-boiling pasteurization steps, boiling, whirlpool steps, and chilling.

<strong>BoilStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase), [StepCommon::StepWithRampTime](./StepCommon.md#stepwithramptime) and [StepCommon::StepWithGravity](./StepCommon.md#stepwithgravity) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
chilling_type
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `batch`<br>&nbsp;∙ `inline`
</td><td style="border: 1px solid black; padding: 6px;">
Chilling type separates batch chilling, eg immersion chillers, where the entire volume of wort is brought down in temperature as a whole, vs inline chilling where the wort is chilled while it is being drained, which can leave a significant amount of hop isomerization occurring in the boil kettle.
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
