# Culture

Collects the attributes of a microbial culture such as a yeast.

<strong>Culture</strong> is a JSON object with all properties from [CultureBase](#culturebase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">temperature_range</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::RangeOfTemperature](Measurement.md#rangeoftemperature)</td><td style="border: 1px solid black; padding: 6px;">The recommended temperature range of fermentation by the culture producer.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">alcohol_tolerance</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The recommended limit of abv by the culture producer before attenuation stops.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">flocculation</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">Enum:<br/>&nbsp;∙ `very low`<br/>
&nbsp;∙ `low`<br/>
&nbsp;∙ `medium low`<br/>
&nbsp;∙ `medium`<br/>
&nbsp;∙ `medium high`<br/>
&nbsp;∙ `high`<br/>
&nbsp;∙ `very high`</td><td style="border: 1px solid black; padding: 6px;">Floculation refers to the ability of yeast to aggregate to form large flocs which drop out of suspension.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">attenuation_range</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::RangeOfPercentage](Measurement.md#rangeofpercentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">notes</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">best_for</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;">Recommended styles for a particular culture.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">max_reuse</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">integer</td><td style="border: 1px solid black; padding: 6px;">Maximum number of times to reuse a culture before a new lab source is recommended.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">pof</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;">A POF+ culture is capable of producing phenols, which is a common distinctive property of saison, and brett yeasts.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">glucoamylase</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;">A glucoamylase positive culture is capable of producing glucoamylase, the enzyme produced through expression of the diastatic gene, which allows yeast to attenuate dextrins and starches leading to a very low FG. This is positive in some saison/brett yeasts as well as the new gulo hybrid by Omega yeast labs.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">inventory</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[CultureInventory](#cultureinventory)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">zymocide</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">object</td><td style="border: 1px solid black; padding: 6px;">Zymocide, also known as killer yeast properties, is common among wine yeasts. There are also some ale and brett yeasts that are immune to some zymocidic properties, these are known as killer neutral.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">zymocide.no1</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">zymocide.no2</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">zymocide.no28</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">zymocide.klus</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">zymocide.neutral</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>


---

# Definitions

## CultureBase

Provides unique properties to identify individual records of a culture.

<strong>CultureBase</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">name</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">culture_type</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">Enum:<br/>&nbsp;∙ `ale`<br/>
&nbsp;∙ `bacteria`<br/>
&nbsp;∙ `brett`<br/>
&nbsp;∙ `champagne`<br/>
&nbsp;∙ `kveik`<br/>
&nbsp;∙ `lacto`<br/>
&nbsp;∙ `lager`<br/>
&nbsp;∙ `malolactic`<br/>
&nbsp;∙ `mixed-culture`<br/>
&nbsp;∙ `other`<br/>
&nbsp;∙ `pedio`<br/>
&nbsp;∙ `spontaneous`<br/>
&nbsp;∙ `wine`</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">form</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">Enum:<br/>&nbsp;∙ `liquid`<br/>
&nbsp;∙ `dry`<br/>
&nbsp;∙ `slant`<br/>
&nbsp;∙ `culture`<br/>
&nbsp;∙ `dregs`</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">producer</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">product_id</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td>
</tr>

## CultureInventory

No description provided for this model.

<strong>CultureInventory</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">liquid</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Volume](Measurement.md#volume)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">dry</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Mass](Measurement.md#mass)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">slant</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Volume](Measurement.md#volume)</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">culture</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Volume](Measurement.md#volume)</td>
</tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
