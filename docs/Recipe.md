# Recipe

The information stored in a beer recipe.

<strong>Recipe</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| type | ✅ | Enum:<br>&nbsp;∙ `cider`<br>&nbsp;∙ `kombucha`<br>&nbsp;∙ `soda`<br>&nbsp;∙ `other`<br>&nbsp;∙ `mead`<br>&nbsp;∙ `wine`<br>&nbsp;∙ `extract`<br>&nbsp;∙ `partial mash`<br>&nbsp;∙ `all grain` |  |
| author | ✅ | string |  |
| batch_size | ✅ | [Measurement::Volume](./Measurement.md#volume) | The volume into the fermenter. |
| efficiency | ✅ | object | Stores each efficiency component. |
| efficiency.conversion |  | [Measurement::Percentage](./Measurement.md#percentage) | The percentage of sugar from the grain yield that is extracted and converted during the mash. |
| efficiency.lauter |  | [Measurement::Percentage](./Measurement.md#percentage) | The percentage of sugar that makes it from the mash tun to the kettle. |
| efficiency.mash |  | [Measurement::Percentage](./Measurement.md#percentage) | The percentage of sugar that makes it from the grain to the kettle. |
| efficiency.brewhouse | ✅ | [Measurement::Percentage](./Measurement.md#percentage) | The percentage of sugar that makes it from the grain to the fermenter. |
| ingredients | ✅ | object | All the recipe's ingredient additions.  Note that these lists are "abbreviated" versions of each ingredient, which saves on repetition when, eg, the same type of hop is added at more then one point.  If you are exporting one or more recipes, you should also export the full versions of their ingredients in the same file. |
| ingredients.fermentable_additions | ✅ | array of [FermentableRecipeAddition](#fermentablerecipeaddition) | All the fermentable additions to the recipe |
| ingredients.hop_additions |  | array of [HopRecipeAddition](#hoprecipeaddition) | All the hop additions to the recipe |
| ingredients.miscellaneous_additions |  | array of [OtherIngredientRecipeAddition](#otheringredientrecipeaddition) | All the miscellaneous item additions to the recipe |
| ingredients.culture_additions |  | array of [CultureRecipeAddition](#culturerecipeaddition) | All the yeast and/or other culture additions to the recipe |
| coauthor |  | string |  |
| created |  | [Measurement::Date](./Measurement.md#date) |  |
| style |  | [Style::StyleBase](./Style.md#stylebase) |  |
| water_profile_base |  | [Water::WaterBase](./Water.md#waterbase) | Optional parameter to specify the starting profile of the brewing water, which may be modified with salts etc to obtain the target profile. |
| water_profile_target |  | [Water::WaterBase](./Water.md#waterbase) | Optional parameter to specify the desired profile of the brewing water, which may be modified with salts etc from the base (starting) profile. |
| mash |  | [Mash](./Mash.md) | This defines the procedure for performing unique mashing processes. |
| boil |  | [Boil](./Boil.md) | Defines the procedure for performing a boil. A boil procedure with no steps is the same as a standard single step boil. |
| fermentation |  | [Fermentation](./Fermentation.md) | FermentationProcedureType defines the procedure for performing fermentation. |
| notes |  | string |  |
| original_gravity |  | [Measurement::Density](./Measurement.md#density) | The gravity of wort when transferred to the fermenter. |
| final_gravity |  | [Measurement::Density](./Measurement.md#density) | The gravity of beer at the end of fermentation. |
| alcohol_by_volume |  | [Measurement::Percentage](./Measurement.md#percentage) |  |
| ibu_estimate |  | [Measurement::Bitterness](./Measurement.md#bitterness) | Estimated bitterness of finished beer. |
| ibu_estimate_formula |  | Enum:<br>&nbsp;∙ `Tinseth`<br>&nbsp;∙ `Rager`<br>&nbsp;∙ `Noonan`<br>&nbsp;∙ `mIBU` | Used to differentiate which IBU formula is being used in a recipe. If formula is modified in any way, eg to support whirlpool/flameout additions etc etc, please use `Other` for transparency. |
| color_estimate |  | [Measurement::Color](./Measurement.md#color) | The color of the finished beer, using SRM or EBC. |
| beer_pH |  | [Measurement::Acidity](./Measurement.md#acidity) | The final beer pH at the end of fermentation. |
| carbonation |  | [Measurement::Carbonation](./Measurement.md#carbonation) | The final carbonation of the beer when packaged or served. |
| apparent_attenuation |  | [Measurement::Percentage](./Measurement.md#percentage) | The total apparent attenuation of the finished beer after fermentation. |
| taste |  | object | Subjective tasting notes, and rating. |
| taste.notes | ✅ | string |  |
| taste.rating | ✅ | number |  |
| calories_per_us_pint |  | number |  |


---

# Component Types

## AdditionSchedule

This object fully describes when, and for how long, a recipe addition should be made, with options for basis on time, gravity, or pH at any process step.

<strong>AdditionSchedule</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| time |  | [Measurement::Time](./Measurement.md#time) | What time during a process step is added, eg a value of 2 days for a dry hop addition would be added 2 days into the fermentation step.  NOTE that, for use::add_to_boil, this is time before the end of the step (or of the boil if no step is specified).  For other values of use, this is time after the start of the step (or of the process if no step is specified). |
| duration |  | [Measurement::Time](./Measurement.md#time) | How long an ingredient addition remains, this was referred to as time in the BeerXML standard. Eg A 40 minute hop boil additions means to boil for 40 minutes, and a 2 day duration for a dry hop means to remove it after 2 days. |
| continuous |  | boolean | A continuous addition is spread out evenly and added during the entire process step.  Eg 60 minute IPA by dogfish head takes all ofthe hop additions and adds them throughout the entire boil. |
| specific_gravity |  | [Measurement::Density](./Measurement.md#density) | Used to indicate when an addition is added based on a desired specific gravity.  Eg Add dry hop at when SG is 1.018. |
| pH |  | [Measurement::Acidity](./Measurement.md#acidity) | Used to indicate when an addition is added based on a desired specific pH.  Eg Add brett when pH is 3.4. |
| step |  | integer | Used to indicate what step this ingredient timing addition is referencing.  Eg A value of 2 for add_to_fermentation would mean to add during the second fermentation step. |
| use |  | Enum:<br>&nbsp;∙ `add_to_mash`<br>&nbsp;∙ `add_to_boil`<br>&nbsp;∙ `add_to_fermentation`<br>&nbsp;∙ `add_to_package` | Differentiates the specific process type when this ingredient addition is used. |

## CultureRecipeAddition

Collects the attributes of each culture ingredient for use in a recipe.

<strong>CultureRecipeAddition</strong> is a JSON object with all properties from [Culture::CultureBase](./Culture.md#culturebase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| attenuation |  | [Measurement::Percentage](./Measurement.md#percentage) | The expected, or measured apparent attenuation for a given culture in a given recipe. In comparison to attenuation range, this is a single value. |
| times_cultured |  | integer |  |
| schedule |  | [AdditionSchedule](#additionschedule) |  |
| cell_count_billions |  | integer |  |
| amount |  | [Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |  |

## FermentableRecipeAddition

Collects the attributes of each fermentable ingredient for use in a recipe fermentable bill.

<strong>FermentableRecipeAddition</strong> is a JSON object with all properties from [Fermentable::FermentableBase](./Fermentable.md#fermentablebase) as well as these additional ones:

| Property | Required? | Type |
| -------- | --------- | ---- |
| amount | ✅ | [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |
| schedule |  | [AdditionSchedule](#additionschedule) |

## HopRecipeAddition

Collects the attributes of each hop ingredient for use in a recipe hop bill.

<strong>HopRecipeAddition</strong> is a JSON object with all properties from [Hop::HopBase](./Hop.md#hopbase) as well as these additional ones:

| Property | Required? | Type |
| -------- | --------- | ---- |
| schedule | ✅ | [AdditionSchedule](#additionschedule) |
| amount | ✅ | [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |

## OtherIngredientRecipeAddition

Collects the attributes of each miscellaneous ingredient for use in a recipe.

<strong>OtherIngredientRecipeAddition</strong> is a JSON object with all properties from [OtherIngredient::OtherIngredientBase](./OtherIngredient.md#otheringredientbase) as well as these additional ones:

| Property | Required? | Type |
| -------- | --------- | ---- |
| schedule |  | [AdditionSchedule](#additionschedule) |
| amount |  | [Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-06-10 at 09:03:35+0200.
