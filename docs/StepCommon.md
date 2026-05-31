# StepCommon

JSON Schema missing a description, provide it using the `description` key in the root of the JSON document.

<strong>Type:</strong> `object(?)`


---

# Definitions

## StepBase

Common attributes of MashStep, BoilStep and FermentationStep.

<strong>StepBase</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">name</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">step_description</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">step_time</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Time](./Measurement.md#time)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">start_temperature</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Temperature](./Measurement.md#temperature)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">end_temperature</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Temperature](./Measurement.md#temperature)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">start_pH</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Acidity](./Measurement.md#acidity)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">end_pH</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Acidity](./Measurement.md#acidity)</td>
</tr>

## StepWithRampTime

Common attribute of MashStep and BoilStep but not FermentationStep.

<strong>StepWithRampTime</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">ramp_time</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Time](./Measurement.md#time)</td><td style="border: 1px solid black; padding: 6px;">The amount of time that passes before this step begins. eg moving from a mash step (step 1) of 148°F, to a new temperature step of 156°F (step 2) may take 8 minutes to heat the mash. Step 2 would have a ramp time of 8 minutes.</td>
</tr>

## StepWithGravity

Common attributes of BoilStep and FermentationStep but not MashStep.

<strong>StepWithGravity</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">start_gravity</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Density](./Measurement.md#density)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">end_gravity</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Density](./Measurement.md#density)</td>
</tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
