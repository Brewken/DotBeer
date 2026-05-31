# Measurement Types

Various types of measurement, and ranges thereof.

In principle, we could have sub-groupings such as "physical quantities" (volume, mass, acidity, etc), "non-physical quantities" (percentage, count, date, etc).  However, this adds complexity to the schema for little gain, because there is nowhere else in the schema where we would rely on such groupings.  So, instead, we keep a flat hierarchy.

In several cases, there is only one possible unit (eg acidity, percentage, count), so it would be possible to omit units altogether.  However, in common with BeerJSON, we retain them for a couple of reasons.  Firstly, it makes the serialisation easier to understand for human readers.  Secondly, it makes things more extendable: eg, if we decided at a future date we would like to support "percentage points" in addition to "percentages", then it's a smaller change to add them.

For Ranges, note that we do not force the same units for lower and upper bounds.  This is partly because it would complicate the schema for only small gain, and partly because it's conceivable that you want different units on min and max (eg if you had a mass range you might want min in grams and max in kilograms).

<strong>Type:</strong> `object(?)`


---

# Definitions

## Acidity

No description provided for this model.

<strong>Acidity</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `pH`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Bitterness

No description provided for this model.

<strong>Bitterness</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `IBUs`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Carbonation

No description provided for this model.

<strong>Carbonation</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `vols`<br>&nbsp;∙ `g/l`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Color

Supports both grain color properties, such as Lovibond, and wort color properties such as SRM and EBC.

<strong>Color</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `EBC`<br>&nbsp;∙ `Lovi`<br>&nbsp;∙ `SRM`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Count

Used where unitless amounts are required, such as 1 apple, or 1 yeast packet.  Note that this _is_ allowed to be fractional because you might want to add 1½ cinnamon sticks or 2.5 packets of yeast.

<strong>Count</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `1`<br>&nbsp;∙ `unit`<br>&nbsp;∙ `each`<br>&nbsp;∙ `dimensionless`<br>&nbsp;∙ `pkg`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Date

To avoid ambiguity, dates are always stored in ISO 8601 format.  The two possibilities here are with and without time of day.

<strong>Date</strong> is a ``string``  matching regular expression [`\d{4}-\d{2}-\d{2}\|\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}`](https://regex101.com/?regex=%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D%7C%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7DT%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7D)

## Density

Sometimes referred to as "gravity" as a shorthand for "specific gravity".  Typically, brewers measure relative density (aka specific gravity) to gauge percent of sugar content (ie plato and brix).

<strong>Density</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `sg`<br>&nbsp;∙ `plato`<br>&nbsp;∙ `brix`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## DiastaticPower

Diastatic power is a measurement of malted grains enzymatic content. A value of 35 Lintner is needed to self convert, while a value of 100 or more is desirable for base malts.

<strong>DiastaticPower</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `Lintner`<br>&nbsp;∙ `WK`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Length

No description provided for this model.

<strong>Length</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `mm`<br>&nbsp;∙ `cm`<br>&nbsp;∙ `m`<br>&nbsp;∙ `in`<br>&nbsp;∙ `ft`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Mass

No description provided for this model.

<strong>Mass</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `mg`<br>&nbsp;∙ `g`<br>&nbsp;∙ `kg`<br>&nbsp;∙ `lb`<br>&nbsp;∙ `oz`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## MassFractionOrConcentration

Strictly speaking, mass concentration (eg mg/l) is different from mass fraction (eg ppm, ppb) but, in the context of brewing, it is usually approximately true that 1 mg/L mass concentration = 1 parts per million (ppm) mass fraction.

<strong>MassFractionOrConcentration</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `ppm`<br>&nbsp;∙ `ppb`<br>&nbsp;∙ `mg/l`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Percentage

No description provided for this model.

<strong>Percentage</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `%`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Pressure

No description provided for this model.

<strong>Pressure</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `kPa`<br>&nbsp;∙ `psi`<br>&nbsp;∙ `bar`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## SpecificHeatCapacity

The amount of heat that must be added to one unit of mass of the substance in order to cause an increase of one unit in temperature.

<strong>SpecificHeatCapacity</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `Cal/(g C)`<br>&nbsp;∙ `J/(kg K)`<br>&nbsp;∙ `BTU/(lb F)`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## SpecificVolume

Specific volume is the reciprocal of density, commonly used for mash thickness.

<strong>SpecificVolume</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `qt/lb`<br>&nbsp;∙ `gal/lb`<br>&nbsp;∙ `gal/oz`<br>&nbsp;∙ `l/g`<br>&nbsp;∙ `l/kg`<br>&nbsp;∙ `floz/oz`<br>&nbsp;∙ `m^3/kg`<br>&nbsp;∙ `ft^3/lb`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Temperature

No description provided for this model.

<strong>Temperature</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `C`<br>&nbsp;∙ `F`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Time

Note this is NOT dates or times of day but length-of-time or elapsed time, eg duration of a mash step, or how long after the start of the boil to add something.

<strong>Time</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `sec`<br>&nbsp;∙ `min`<br>&nbsp;∙ `hr`<br>&nbsp;∙ `day`<br>&nbsp;∙ `week`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
integer
</td></tr>

## VersionNumber

We use semantic versioning, which encodes a version by a three-part version number (Major.Minor.Patch)

<strong>VersionNumber</strong> is a ``string``  matching regular expression [`\d+[.]\d+[.]\d+`](https://regex101.com/?regex=%5Cd%2B%5B.%5D%5Cd%2B%5B.%5D%5Cd%2B)

## Viscosity

Viscosity of fluids

<strong>Viscosity</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `cP`<br>&nbsp;∙ `mPa-s`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## Volume

No description provided for this model.

<strong>Volume</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
unit
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br>&nbsp;∙ `ml`<br>&nbsp;∙ `l`<br>&nbsp;∙ `tsp`<br>&nbsp;∙ `tbsp`<br>&nbsp;∙ `floz`<br>&nbsp;∙ `cup`<br>&nbsp;∙ `pt`<br>&nbsp;∙ `qt`<br>&nbsp;∙ `gal`<br>&nbsp;∙ `bbl`<br>&nbsp;∙ `itsp`<br>&nbsp;∙ `itbsp`<br>&nbsp;∙ `ifloz`<br>&nbsp;∙ `icup`<br>&nbsp;∙ `ipt`<br>&nbsp;∙ `iqt`<br>&nbsp;∙ `igal`<br>&nbsp;∙ `ibbl`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
value
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td></tr>

## RangeOfBitterness

No description provided for this model.

<strong>RangeOfBitterness</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
minimum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Bitterness](#bitterness)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
maximum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Bitterness](#bitterness)
</td></tr>

## RangeOfCarbonation

No description provided for this model.

<strong>RangeOfCarbonation</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
minimum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Carbonation](#carbonation)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
maximum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Carbonation](#carbonation)
</td></tr>

## RangeOfTemperature

No description provided for this model.

<strong>RangeOfTemperature</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
minimum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Temperature](#temperature)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
maximum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Temperature](#temperature)
</td></tr>

## RangeOfColor

No description provided for this model.

<strong>RangeOfColor</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
minimum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Color](#color)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
maximum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Color](#color)
</td></tr>

## RangeOfDensity

No description provided for this model.

<strong>RangeOfDensity</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
minimum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Density](#density)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
maximum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Density](#density)
</td></tr>

## RangeOfPercentage

No description provided for this model.

<strong>RangeOfPercentage</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
minimum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Percentage](#percentage)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
maximum
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Percentage](#percentage)
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
