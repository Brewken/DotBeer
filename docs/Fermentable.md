# Fermentable

Collects the attributes of a fermentable ingredient to store as record information.

<strong>Fermentable</strong> is a JSON object with all properties from [FermentableBase](#fermentablebase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">notes</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">moisture</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">alpha_amylase</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">number</td><td style="border: 1px solid black; padding: 6px;">Where diastatic power gives the total amount of all enzymes, alpha amylase, also known as dextrinizing units, refers to only the total amount of alpa amylase in the malted grain. A value of 25-50 is desirable for base malt.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">diastatic_power</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::DiastaticPower](Measurement.md#diastaticpower)</td><td style="border: 1px solid black; padding: 6px;">Diastatic power is a measurement of malted grains enzymatic content. A value of 35 Lintner is needed to self convert, while a value of 100 or more is desirable.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">protein</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The percentage of protein. Higher values may indicate a possibility of haze, or lautering issues.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">kolbach_index</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The Kolbach Index, also known as soluble to total ratio of nitrogen or protein, is used to indicate the degree of malt modification. A value above 35% is desired for simple single infusion mashing, undermodified malt may require multiple step mashes or decoction.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">max_in_batch</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The recommended maximum percentage to use in a grain bill.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">recommend_mash</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">boolean</td><td style="border: 1px solid black; padding: 6px;">True if the fermentable must be mashed, false if it can be steeped.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">inventory</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[FermentableInventory](#fermentableinventory)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">glassy</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">Used to indicate the 'crystallized' percentage of starches for crystal malts.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">plump</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The percentage of grain that masses through sieves with gaps of 7/64 and 6/64, desired values of 80% or higher which indicate plump kernels.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">half</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">mealy</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The opposite of glassy, a mealy kernel is one that is not glassy. Base malt should be at least 90%, single step mashes generally require 95% or higher.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">thru</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The Percentage of grain that makes it through a thin mesh screen, typically 5/64 inch. Values less than 3% are desired.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">friability</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">Friability is the measure of a malts ability to crumble during the crush, and is used as an indicator for easy gelatinization of the grain and starches, as well as modification of the malt. Value of 85% of higher indicates a well modified malt and is suitable for single step mashes. Lower values may require a step mash.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">di_pH</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Acidity](Measurement.md#acidity)</td><td style="border: 1px solid black; padding: 6px;">The pH of the resultant wort for 1 lb of grain mashed in 1 gallon of distilled water. Used in many water chemistry / mash pH prediction software.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">viscosity</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Viscosity](Measurement.md#viscosity)</td><td style="border: 1px solid black; padding: 6px;">The measure of wort viscosity, typically associated with the breakdown of beta-glucans. The higher the viscosity, the greater the need for a glucan rest and the less suitable for a fly sparge.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">dms_p</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](Measurement.md#massfractionorconcentration)</td><td style="border: 1px solid black; padding: 6px;">The amount of DMS precursors, namely S-methyl methionine (SMM) and dimethyl sulfoxide (DMSO) in the malt which convert to dimethyl sulfide (DMS).</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">fan</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](Measurement.md#massfractionorconcentration)</td><td style="border: 1px solid black; padding: 6px;">Free Amino Nitrogen (FAN) is a critical yeast nutrient. Typical values for base malt is 170.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">fermentability</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">Fermentability - Used in Extracts to indicate a baseline typical apparent attenuation for a typical medium attenuation yeast.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">beta_glucan</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::MassFractionOrConcentration](Measurement.md#massfractionorconcentration)</td><td style="border: 1px solid black; padding: 6px;">Values of 180 or more may suggest a glucan rest and avoiding fly sparging.</td>
</tr>


---

# Definitions

## FermentableBase

FermentableBase provides unique properties to identify individual records of fermentable ingredients.

<strong>FermentableBase</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">name</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">type</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">Enum:<br/>&nbsp;∙ `dry extract`<br/>
&nbsp;∙ `extract`<br/>
&nbsp;∙ `grain`<br/>
&nbsp;∙ `sugar`<br/>
&nbsp;∙ `fruit`<br/>
&nbsp;∙ `juice`<br/>
&nbsp;∙ `honey`<br/>
&nbsp;∙ `other`</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">yield</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">object</td><td style="border: 1px solid black; padding: 6px;">The potential yield of the fermentable ingredient, supporting SG, or percentage. eg 1.037 or 80% are valid yield types.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">yield.fine_grind</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">Percentage yield, compared to sucrose, of a fine grind. eg 80%</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">yield.coarse_grind</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">Percentage yield, compared to sucrose, of a coarse grind. eg 78%</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">yield.fine_coarse_difference</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Percentage](Measurement.md#percentage)</td><td style="border: 1px solid black; padding: 6px;">The difference between fine and coarse grind, a difference more than 2 percent can indicate a protein or step mash may be desirable. eg 2%.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">yield.potential</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Density](Measurement.md#density)</td><td style="border: 1px solid black; padding: 6px;">The potential yield of the fermentable ingredient for 1 lb of grain mashed in 1 gallon of water. eg 1.037</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">color</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::Color](Measurement.md#color)</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">origin</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">producer</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">product_id</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">grain_group</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">Enum:<br/>&nbsp;∙ `base`<br/>
&nbsp;∙ `caramel`<br/>
&nbsp;∙ `flaked`<br/>
&nbsp;∙ `roasted`<br/>
&nbsp;∙ `specialty`<br/>
&nbsp;∙ `smoked`<br/>
&nbsp;∙ `adjunct`</td><td style="border: 1px solid black; padding: 6px;"></td>
</tr>

## FermentableInventory

No description provided for this model.

<strong>FermentableInventory</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">amount</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Measurement::Mass](Measurement.md#mass) or [Measurement::Volume](Measurement.md#volume)</td>
</tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
