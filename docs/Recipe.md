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
| ingredients.miscellaneous_additions |  | array of [MiscIngredientRecipeAddition](#miscingredientrecipeaddition) | All the miscellaneous item additions to the recipe |
| ingredients.culture_additions |  | array of [CultureRecipeAddition](#culturerecipeaddition) | All the yeast and/or other culture additions to the recipe |
| coauthor |  | string |  |
| created |  | [Measurement::Date](./Measurement.md#date) |  |
| style |  | [Style::StyleBase](./Style.md#stylebase) |  |
| water_base |  | [Water::WaterBase](./Water.md#waterbase) | Optional parameter to specify the starting profile of the brewing water, which may be modified with salts etc to obtain the target profile. |
| water_target |  | [Water::WaterBase](./Water.md#waterbase) | Optional parameter to specify the desired profile of the brewing water, which may be modified with salts etc from the base (starting) profile. |
| ro_water_mash |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage of the mash water that is reverse-osmosis (rather than the same profile as `water_base`).  If this field is not present, a value of 0.0 may be assumed. |
| ro_water_sparge |  | [Measurement::Percentage](./Measurement.md#percentage) | Percentage of the sparge water that is reverse-osmosis (rather than the same profile as `water_base`).  If this field is not present, a value of 0.0 may be assumed. |
| mash |  | [Mash](./Mash.md) | This defines the procedure for performing unique mashing processes. |
| boil |  | [Boil](./Boil.md) | Defines the procedure for performing a boil. A boil procedure with no steps is the same as a standard single step boil. |
| fermentation |  | [Fermentation](./Fermentation.md) | FermentationProcedureType defines the procedure for performing fermentation. |
| notes |  | string |  |
| original_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | The gravity of wort when transferred to the fermenter. |
| final_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | The gravity of beer at the end of fermentation. |
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
| brew_logs |  | array of [BrewLog](#brewlog) | Records of individual brews of this recipe |


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
| specific_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | Used to indicate when an addition is added based on a desired specific gravity.  Eg Add dry hop at when SG is 1.018. |
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

## MiscIngredientRecipeAddition

Collects the attributes of each miscellaneous ingredient for use in a recipe.

<strong>MiscIngredientRecipeAddition</strong> is a JSON object with all properties from [MiscIngredient::MiscIngredientBase](./MiscIngredient.md#miscingredientbase) as well as these additional ones:

| Property | Required? | Type |
| -------- | --------- | ---- |
| schedule |  | [AdditionSchedule](#additionschedule) |
| amount |  | [Measurement::Count](./Measurement.md#count) or [Measurement::Mass](./Measurement.md#mass) or [Measurement::Volume](./Measurement.md#volume) |

## BrewLog

Record of a "brewday", ie of an individual brew of a recipe.  Note that:<br> • Fields beginning with "expected_" are values taken rom the Recipe (either directly or by calculation)<br> • Fields beginning with "measured_" are supplied by the brewer for this batch -- eg measured OG and FG<br> • Fields beginning with "computed_" are derived from values supplied by the brewer -- eg ABV calculated from measured OG and FG<br>Strictly speaking, "expected_" and "computed_" fields are not needed because they can be derived from other information.  However, we include them because (a) a recipe might have been modified after a brewday and (b) some calculations (eg alcohol by volume) might be done differently by different programs.

<strong>BrewLog</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| batch_number | ✅ | string | The brewer's own unique identifier for this brew.  It can contain numbers and/or letters and/or symbols, so, "number" might seem a bit of a misnomer; nonetheless, it is the standard term for such an identifying code. |
| brew_date | ✅ | [Measurement::Date](./Measurement.md#date) | The date of the "brewday" |
| expected_pre_boil_gravity_sg | ✅ | [Measurement::Gravity](./Measurement.md#gravity) | Expected (planned) pre-boil specific gravity |
| expected_mash_final_temp_c | ✅ | [Measurement::Temperature](./Measurement.md#temperature) | Expected (planned) final mash temperature (before any mash out) |
| expected_original_gravity | ✅ | [Measurement::Gravity](./Measurement.md#gravity) | Expected (planned) original (post-boil, pre-fermentation) specific gravity |
| expected_volume_into_fermentor | ✅ | [Measurement::Volume](./Measurement.md#volume) | Expected (planned) volume of wort into fermentor |
| expected_final_gravity | ✅ | [Measurement::Gravity](./Measurement.md#gravity) | Expected (planned) final (post-fermentation) specific gravity |
| expected_alcohol_by_volume | ✅ | [Measurement::Percentage](./Measurement.md#percentage) | Expected alcohol by volume based on the recipe OG |
| expected_attenuation | ✅ | [Measurement::Percentage](./Measurement.md#percentage) | Expected attenuation from the recipe |
| expected_efficiency | ✅ | [Measurement::Percentage](./Measurement.md#percentage) | Expected brewhouse (ie overall) efficiency from the Recipe, capturing the combined impact of mash conversion, lautering, kettle losses, and transfer |
| ferment_date |  | [Measurement::Date](./Measurement.md#date) | The date fermentation was deemed finished and final gravity readings were taken |
| notes |  | string |  |
| measured_pre_boil_gravity_sg |  | [Measurement::Gravity](./Measurement.md#gravity) | Actual (measured) pre-boil specific gravity |
| expected_pre_boil_volume |  | [Measurement::Volume](./Measurement.md#volume) | Expected (planned) volume of wort to be collected from mash into boil kettle |
| measured_pre_boil_volume |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) volume of wort collected from mash into boil kettle |
| expected_strike_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Expected (planned) strike water temperature (ie water temperature immediately prior to adding grains at mash start) |
| measured_strike_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Actual (measured) strike water temperature (ie water temperature immediately prior to adding grains at mash start) |
| measured_mash_final_temp_c |  | [Measurement::Temperature](./Measurement.md#temperature) | Actual (measured) final mash temperature (before any mash out) |
| measured_original_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | Actual (measured) original (post-boil, pre-fermentation) specific gravity |
| measured_post_boil_volume |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) volume of wort in kettle after boil |
| measured_volume_into_fermentor |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) volume of wort into fermentor |
| measured_pitch_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Actual (measured) temperature of wort when yeast is pitched |
| measured_final_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | Actual (measured) final (post-fermentation) specific gravity |
| measured_final_volume |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) final (post-fermentation) volume |
| computed_alcohol_by_volume |  | [Measurement::Percentage](./Measurement.md#percentage) | Actual alcohol by volume based on "original" and "final" gravity readings |
| computed_attenuation |  | [Measurement::Percentage](./Measurement.md#percentage) | Actual attenuation based on gravity readings |
| computed_efficiency |  | [Measurement::Percentage](./Measurement.md#percentage) | Actual brewhouse (ie overall) efficiency based on gravity readings |
| computed_pre_boil_efficiency |  | [Measurement::Percentage](./Measurement.md#percentage) | Actual pre-boil (aka "into boil kettle") efficiency, measuring the percentage of total available sugars that made it into the kettle |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.3.0) on 2026-07-08 at 08:57:35+0200.
