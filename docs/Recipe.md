# Recipe

The information stored in a beer recipe.

<strong>Recipe</strong> is a JSON object with the following properties:

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
type
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br/>&nbsp;∙ `cider`<br/>
&nbsp;∙ `kombucha`<br/>
&nbsp;∙ `soda`<br/>
&nbsp;∙ `other`<br/>
&nbsp;∙ `mead`<br/>
&nbsp;∙ `wine`<br/>
&nbsp;∙ `extract`<br/>
&nbsp;∙ `partial mash`<br/>
&nbsp;∙ `all grain`
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
author
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
batch_size
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Volume](./Measurement.md#volume)
</td><td style="border: 1px solid black; padding: 6px;">
The volume into the fermenter.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
efficiency
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
object
</td><td style="border: 1px solid black; padding: 6px;">
Stores each efficiency component.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
efficiency.conversion
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Percentage](./Measurement.md#percentage)
</td><td style="border: 1px solid black; padding: 6px;">
The percentage of sugar from the grain yield that is extracted and converted during the mash.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
efficiency.lauter
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Percentage](./Measurement.md#percentage)
</td><td style="border: 1px solid black; padding: 6px;">
The percentage of sugar that makes it from the mash tun to the kettle.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
efficiency.mash
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Percentage](./Measurement.md#percentage)
</td><td style="border: 1px solid black; padding: 6px;">
The percentage of sugar that makes it from the grain to the kettle.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
efficiency.brewhouse
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Percentage](./Measurement.md#percentage)
</td><td style="border: 1px solid black; padding: 6px;">
The percentage of sugar that makes it from the grain to the fermenter.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ingredients
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
object
</td><td style="border: 1px solid black; padding: 6px;">
All the recipe's ingredient additions.  Note that these lists are "abbreviated" versions of each ingredient, which saves on repetition when, eg, the same type of hop is added at more then one point.  If you are exporting one or more recipes, you should also export the full versions of their ingredients in the same file.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ingredients.fermentable_additions
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[FermentableRecipeAddition](#fermentablerecipeaddition)
</td><td style="border: 1px solid black; padding: 6px;">
All the fermentable additions to the recipe
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ingredients.hop_additions
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[HopRecipeAddition](#hoprecipeaddition)
</td><td style="border: 1px solid black; padding: 6px;">
All the hop additions to the recipe
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ingredients.miscellaneous_additions
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[OtherIngredientRecipeAddition](#otheringredientrecipeaddition)
</td><td style="border: 1px solid black; padding: 6px;">
All the miscellaneous item additions to the recipe
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ingredients.culture_additions
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[CultureRecipeAddition](#culturerecipeaddition)
</td><td style="border: 1px solid black; padding: 6px;">
All the yeast and/or other culture additions to the recipe
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
coauthor
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
created
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Date](./Measurement.md#date)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
style
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Style::StyleBase](./Style.md#stylebase)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
water_profile_base
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Water::WaterBase](./Water.md#waterbase)
</td><td style="border: 1px solid black; padding: 6px;">
Optional parameter to specify the starting profile of the brewing water, which may be modified with salts etc to obtain the target profile.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
water_profile_target
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Water::WaterBase](./Water.md#waterbase)
</td><td style="border: 1px solid black; padding: 6px;">
Optional parameter to specify the desired profile of the brewing water, which may be modified with salts etc from the base (starting) profile.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
mash
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Mash](./Mash.md)
</td><td style="border: 1px solid black; padding: 6px;">
This defines the procedure for performing unique mashing processes.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
boil
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Boil](./Boil.md)
</td><td style="border: 1px solid black; padding: 6px;">
Defines the procedure for performing a boil. A boil procedure with no steps is the same as a standard single step boil.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
fermentation
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Fermentation](./Fermentation.md)
</td><td style="border: 1px solid black; padding: 6px;">
FermentationProcedureType defines the procedure for performing fermentation.
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
original_gravity
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Density](./Measurement.md#density)
</td><td style="border: 1px solid black; padding: 6px;">
The gravity of wort when transferred to the fermenter.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
final_gravity
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Density](./Measurement.md#density)
</td><td style="border: 1px solid black; padding: 6px;">
The gravity of beer at the end of fermentation.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
alcohol_by_volume
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Percentage](./Measurement.md#percentage)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ibu_estimate
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Bitterness](./Measurement.md#bitterness)
</td><td style="border: 1px solid black; padding: 6px;">
Estimated bitterness of finished beer.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
ibu_estimate_formula
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br/>&nbsp;∙ `Tinseth`<br/>
&nbsp;∙ `Rager`<br/>
&nbsp;∙ `Noonan`<br/>
&nbsp;∙ `mIBU`
</td><td style="border: 1px solid black; padding: 6px;">
Used to differentiate which IBU formula is being used in a recipe. If formula is modified in any way, eg to support whirlpool/flameout additions etc etc, please use `Other` for transparency.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
color_estimate
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Color](./Measurement.md#color)
</td><td style="border: 1px solid black; padding: 6px;">
The color of the finished beer, using SRM or EBC.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
beer_pH
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Acidity](./Measurement.md#acidity)
</td><td style="border: 1px solid black; padding: 6px;">
The final beer pH at the end of fermentation.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
carbonation
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Carbonation](./Measurement.md#carbonation)
</td><td style="border: 1px solid black; padding: 6px;">
The final carbonation of the beer when packaged or served.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
apparent_attenuation
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Percentage](./Measurement.md#percentage)
</td><td style="border: 1px solid black; padding: 6px;">
The total apparent attenuation of the finished beer after fermentation.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
taste
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
object
</td><td style="border: 1px solid black; padding: 6px;">
Subjective tasting notes, and rating.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
taste.notes
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
taste.rating
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
number
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
calories_per_us_pint
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
number
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>


---

# Definitions

## AdditionSchedule

This object fully describes when, and for how long, a recipe addition should be made, with options for basis on time, gravity, or pH at any process step.

<strong>AdditionSchedule</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
time
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Time](./Measurement.md#time)
</td><td style="border: 1px solid black; padding: 6px;">
What time during a process step is added, eg a value of 2 days for a dry hop addition would be added 2 days into the fermentation step.  NOTE that, for use::add_to_boil, this is time before the end of the step (or of the boil if no step is specified).  For other values of use, this is time after the start of the step (or of the process if no step is specified).
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
duration
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Time](./Measurement.md#time)
</td><td style="border: 1px solid black; padding: 6px;">
How long an ingredient addition remains, this was referred to as time in the BeerXML standard. Eg A 40 minute hop boil additions means to boil for 40 minutes, and a 2 day duration for a dry hop means to remove it after 2 days.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
continuous
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
boolean
</td><td style="border: 1px solid black; padding: 6px;">
A continuous addition is spread out evenly and added during the entire process step.  Eg 60 minute IPA by dogfish head takes all ofthe hop additions and adds them throughout the entire boil.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
specific_gravity
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Density](./Measurement.md#density)
</td><td style="border: 1px solid black; padding: 6px;">
Used to indicate when an addition is added based on a desired specific gravity.  Eg Add dry hop at when SG is 1.018.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
pH
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Acidity](./Measurement.md#acidity)
</td><td style="border: 1px solid black; padding: 6px;">
Used to indicate when an addition is added based on a desired specific pH.  Eg Add brett when pH is 3.4.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
step
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
integer
</td><td style="border: 1px solid black; padding: 6px;">
Used to indicate what step this ingredient timing addition is referencing.  Eg A value of 2 for add_to_fermentation would mean to add during the second fermentation step.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
use
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
Enum:<br/>&nbsp;∙ `add_to_mash`<br/>
&nbsp;∙ `add_to_boil`<br/>
&nbsp;∙ `add_to_fermentation`<br/>
&nbsp;∙ `add_to_package`
</td><td style="border: 1px solid black; padding: 6px;">
Differentiates the specific process type when this ingredient addition is used.
</td></tr>

## CultureRecipeAddition

Collects the attributes of each culture ingredient for use in a recipe.

<strong>CultureRecipeAddition</strong> is a JSON object with all properties from [Culture::CultureBase](./Culture.md#culturebase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
attenuation
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Percentage](./Measurement.md#percentage)
</td><td style="border: 1px solid black; padding: 6px;">
The expected, or measured apparent attenuation for a given culture in a given recipe. In comparison to attenuation range, this is a single value.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
times_cultured
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
integer
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
schedule
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[AdditionSchedule](#additionschedule)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
cell_count_billions
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
integer
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
amount
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>

## FermentableRecipeAddition

Collects the attributes of each fermentable ingredient for use in a recipe fermentable bill.

<strong>FermentableRecipeAddition</strong> is a JSON object with all properties from [Fermentable::FermentableBase](./Fermentable.md#fermentablebase) as well as these additional ones:

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
[Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
schedule
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[AdditionSchedule](#additionschedule)
</td></tr>

## HopRecipeAddition

Collects the attributes of each hop ingredient for use in a recipe hop bill.

<strong>HopRecipeAddition</strong> is a JSON object with all properties from [Hop::HopBase](./Hop.md#hopbase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
schedule
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[AdditionSchedule](#additionschedule)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
amount
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume)
</td></tr>

## OtherIngredientRecipeAddition

Collects the attributes of each miscellaneous ingredient for use in a recipe.

<strong>OtherIngredientRecipeAddition</strong> is a JSON object with all properties from [OtherIngredient::OtherIngredientBase](./OtherIngredient.md#otheringredientbase) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
schedule
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[AdditionSchedule](#additionschedule)
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
amount
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume)
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
