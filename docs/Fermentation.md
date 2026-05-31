# Fermentation

A fermentation procedure, which can be used by multiple recipes.

<strong>Fermentation</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
name
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
fermentation_steps
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[FermentationStep](#fermentationstep)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
fermentation_description
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


---

# Definitions

## FermentationStep

Individual step of a fermentation.

<strong>FermentationStep</strong> is a JSON object with all properties from [StepCommon::StepBase](./StepCommon.md#stepbase) and [StepCommon::StepWithGravity](./StepCommon.md#stepwithgravity) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
free_rise
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
boolean
</td><td style="border: 1px solid black; padding: 6px;">
Free rise is used to indicate a fermentation step where the exothermic fermentation is allowed to raise the temperature without restriction This is either True or false.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
vessel
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
