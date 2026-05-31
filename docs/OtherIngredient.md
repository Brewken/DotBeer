# OtherIngredient

Collects the attributes of an ingredient to store as record information.

<strong>OtherIngredient</strong> is a JSON object with all properties from [OtherIngredientBase](#otheringredientbase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
use_for
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
Used to describe the purpose of the miscellaneous ingredient, e.g. whirlfloc is used for clarity.
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
<tr>
<td style="border: 1px solid black; padding: 6px;">
inventory
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[OtherIngredientInventory](#otheringredientinventory)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>


---

# Definitions

## OtherIngredientBase

Ingredients that are not hops, fermentables, yeasts/cultures or water.  Some people would call these "other ingredients" "non-fermentable adjuncts", but there are also narrower definitions of "adjunct", so we do not use that term.

<strong>OtherIngredientBase</strong> is a JSON object with the following properties:

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
type
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br/>&nbsp;∙ `spice`<br/>
&nbsp;∙ `fining`<br/>
&nbsp;∙ `water agent`<br/>
&nbsp;∙ `herb`<br/>
&nbsp;∙ `flavor`<br/>
&nbsp;∙ `wood`<br/>
&nbsp;∙ `other`
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
producer
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
product_id
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td></tr>

## OtherIngredientInventory

No description provided for this model.

<strong>OtherIngredientInventory</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
amount
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume)
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
