# Style

The full definition of a Style categorization

<strong>Style</strong> is a JSON object with all properties from [StyleBase](#stylebase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
original_gravity
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::RangeOfDensity](./Measurement.md#rangeofdensity)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
final_gravity
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::RangeOfDensity](./Measurement.md#rangeofdensity)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
international_bitterness_units
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::RangeOfBitterness](./Measurement.md#rangeofbitterness)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
color
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::RangeOfColor](./Measurement.md#rangeofcolor)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
carbonation
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::RangeOfCarbonation](./Measurement.md#rangeofcarbonation)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
alcohol_by_volume
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::RangeOfPercentage](./Measurement.md#rangeofpercentage)
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
aroma
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
appearance
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
flavor
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
mouthfeel
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
overall_impression
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ingredients
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
examples
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>


---

# Definitions

## StyleBase

The descriptive base type for both style guideline records, and recipe style provisions. Provides unique properties to identify individual styles

<strong>StyleBase</strong> is a JSON object with the following properties:

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
category
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
style_guide
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
style_type
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `beer`<br>&nbsp;∙ `cider`<br>&nbsp;∙ `kombucha`<br>&nbsp;∙ `mead`<br>&nbsp;∙ `other`<br>&nbsp;∙ `soda`<br>&nbsp;∙ `wine`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
category_number
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
integer
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
style_letter
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
 matching regular expression [`[A-Z ]`](https://regex101.com/?regex=%5BA-Z+%5D)
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
