# DotBeer File Format

A free and open serialisation format for beer recipes, ingredients and related data

<strong>DotBeer File Format</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">object</td><td style="border: 1px solid black; padding: 6px;">Root element of all DotBeer documents.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.version</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::VersionNumber](./Measurement.md#versionnumber)</td><td style="border: 1px solid black; padding: 6px;">DotBeer schema version used to create the file.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.output_by</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">string</td><td style="border: 1px solid black; padding: 6px;">Application that wrote the file -- eg Brewtarget 5.2.1.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.timestamp</td><td style="border: 1px solid black; padding: 6px;">✅</td><td style="border: 1px solid black; padding: 6px;">[Measurement::Date](./Measurement.md#date)</td><td style="border: 1px solid black; padding: 6px;">Date and time file was created.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.hops</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Hop](./Hop.md)</td><td style="border: 1px solid black; padding: 6px;">Records detailing properties of unique hop varieties.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.fermentables</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Fermentable](./Fermentable.md)</td><td style="border: 1px solid black; padding: 6px;">Records for any ingredient that contributes to the gravity of the beer.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.other_ingredients</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[OtherIngredient](./OtherIngredient.md)</td><td style="border: 1px solid black; padding: 6px;">Records for adjuncts which do not contribute to the gravity of the beer.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.cultures</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Culture](./Culture.md)</td><td style="border: 1px solid black; padding: 6px;">Records detailing the wide array of unique cultures.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.waters</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Water](./Water.md)</td><td style="border: 1px solid black; padding: 6px;">Records for water profiles used in brewing.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.mashes</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Mash](./Mash.md)</td><td style="border: 1px solid black; padding: 6px;">Common mashing procedures.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.boils</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Boil](./Boil.md)</td><td style="border: 1px solid black; padding: 6px;">Common boil procedures.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.fermentations</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Fermentation](./Fermentation.md)</td><td style="border: 1px solid black; padding: 6px;">Common fermentation procedures.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.styles</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Style](./Style.md)</td><td style="border: 1px solid black; padding: 6px;">Details of judging guidelines for individual beer styles.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.equipments</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Equipment](./Equipment.md)</td><td style="border: 1px solid black; padding: 6px;">Provides necessary information for brewing equipment.</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">DotBeer.recipes</td><td style="border: 1px solid black; padding: 6px;"></td><td style="border: 1px solid black; padding: 6px;">[Recipe](./Recipe.md)</td><td style="border: 1px solid black; padding: 6px;">Records containing a minimal collection of the description of ingredients, procedures and other required parameters necessary to recreate a batch of beer.</td>
</tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
