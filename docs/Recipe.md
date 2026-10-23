# Recipe

The information stored in a beer recipe.

<strong>Recipe</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| recipe_type | ✅ | Enum:<br>&nbsp;∙ `cider`<br>&nbsp;∙ `kombucha`<br>&nbsp;∙ `soda`<br>&nbsp;∙ `other`<br>&nbsp;∙ `mead`<br>&nbsp;∙ `wine`<br>&nbsp;∙ `extract`<br>&nbsp;∙ `partial mash`<br>&nbsp;∙ `all grain` | The kind of beverage the recipe produces and, for beer, the mashing approach it uses. |
| author | ✅ | string | The person (or organisation) who wrote the recipe. |
| batch_size | ✅ | [Measurement::Volume](./Measurement.md#volume) | The volume into the fermentation vessel. |
| efficiency | ✅ | object | Stores each efficiency component. |
| efficiency.brewhouse | ✅ | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The percentage of the available sugar that makes it from the fermentables into the fermenter.  This only applies to fermentables whose sugars have to be extracted (eg grain that is mashed or steeped).  The sugar in extracts and sugars is assumed to be fully available.  So, in an extract recipe with no grain, this value has no effect. |
| ingredients | ✅ | object | All the recipe's ingredient additions.  Note that these lists are cross-references (via "local IDs") to ingredient definitions that must appear in the same file.  This saves on repetition when, eg, the same type of hop is added at more than one point.  If you are exporting one or more recipes, you must also export the full versions of their ingredients in the same file. |
| ingredients.fermentable_additions | ✅ | array of [FermentableRecipeAddition](#fermentablerecipeaddition) | All the fermentable additions to the recipe |
| ingredients.hop_additions |  | array of [HopRecipeAddition](#hoprecipeaddition) | All the hop additions to the recipe |
| ingredients.misc_additions |  | array of [MiscRecipeAddition](#miscrecipeaddition) | All the miscellaneous item additions to the recipe |
| ingredients.culture_additions |  | array of [CultureRecipeAddition](#culturerecipeaddition) | All the yeast and/or other culture additions to the recipe |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Recipe object. |
| coauthor |  | string | An additional author of the recipe. |
| created |  | [Measurement::DateOrDateTimeLocal](./Measurement.md#dateordatetimelocal) | When the recipe was created. |
| style_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | Local ID of the style of this recipe.  (Obviously the style in question must be in the "styles" section of the same dotBeer file.) |
| equipment_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | Local ID of the equipment for this recipe.  (Obviously the equipment in question must be in the "equipments" section of the same dotBeer file.) |
| water_base_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | Optional parameter to specify the Local ID of the starting profile of the brewing water, which may be modified with salts etc to obtain the target profile. |
| water_target_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | Optional parameter to specify the Local ID of the desired profile of the brewing water, which may be modified with salts etc from the base (starting) profile. |
| ro_water_mash |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Percentage of the mash water that is reverse-osmosis (rather than the same profile as `water_base_id`).  If this field is not present, a value of 0.0 may be assumed. |
| ro_water_sparge |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Percentage of the sparge water that is reverse-osmosis (rather than the same profile as `water_base_id`).  If this field is not present, a value of 0.0 may be assumed. |
| mash_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | Local ID of the mash procedure used in this recipe.  (Obviously the mash in question must be in the "mashes" section of the same dotBeer file.) |
| boil_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | Local ID of the boil procedure used in this recipe.  (Obviously the boil in question must be in the "boils" section of the same dotBeer file.) |
| fermentation_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | Local ID of the fermentation procedure used in this recipe.  (Obviously the fermentation in question must be in the "fermentations" section of the same dotBeer file.) |
| notes |  | string |  |
| original_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | The expected gravity of wort when transferred to the fermenter.  Typically this and `final_gravity` are calculated values, so they are written out for information but ignored (or overwritten by a calculated value) for recipes read in from a file. |
| final_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | The expected gravity of beer at the end of fermentation.  Comments about `original_gravity` apply equally here. |
| alcohol_by_volume |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The expected alcohol by volume of the finished beer, typically calculated from `original_gravity` and `final_gravity`.  Comments about `original_gravity` apply equally here.  (Measured values for an actual brew of the recipe go in its brew log.) |
| ibu_estimate |  | [Measurement::Bitterness](./Measurement.md#bitterness) | Estimated bitterness of finished beer. |
| ibu_estimate_formula |  | Enum:<br>&nbsp;∙ `Tinseth`<br>&nbsp;∙ `Rager`<br>&nbsp;∙ `Noonan`<br>&nbsp;∙ `mIBU`<br>&nbsp;∙ `Garetz`<br>&nbsp;∙ `SMPH`<br>&nbsp;∙ `Daniel`<br>&nbsp;∙ `other` | Used to differentiate which IBU formula is being used in a recipe. |
| color_estimate |  | [Measurement::Color](./Measurement.md#color) | The color of the finished beer, using SRM or EBC. |
| beer_pH |  | [Measurement::Acidity](./Measurement.md#acidity) | The final beer pH at the end of fermentation. |
| carbonation |  | [Measurement::Carbonation](./Measurement.md#carbonation) | The final carbonation of the beer when packaged or served. |
| apparent_attenuation |  | [Measurement::PercentageNoMax](./Measurement.md#percentagenomax) | The total apparent attenuation of the finished beer after fermentation.  (This can be more than 100% if the final gravity is below 1.000 SG.) |
| taste |  | object | Subjective tasting notes, and rating. |
| taste.notes | ✅ | string |  |
| taste.rating | ✅ | `0.0 <= x <= 50.0` | Number between zero and 50 denoting the taste rating – corresponds to the 50 point BJCP rating system. |
| energy_content |  | [Measurement::EnergyPerVolume](./Measurement.md#energypervolume) | Estimate of the energy content of this beer (as used on nutritional labelling).  Typically calculated. |
| instructions |  | array of [Instruction](#instruction) | Records of individual instructions for this recipe |
| brew_logs |  | array of [BrewLog](#brewlog) | Records of individual brews of this recipe |


---

# Component Types

## AdditionSchedule

This object fully describes when, and for how long, a recipe addition should be made, with options for basis on time, gravity, or pH at any process step.

Hop additions that BeerXML would call *first wort* and *aroma* (eg whirlpool, hop stand or flameout additions) are expressed through the step of the boil in which they are made.  By convention, a boil has a pre-boil step (ramping up from mash temperature), then the boil proper, then one or more post-boil steps (cooling).

A boil step is part of the *boil proper* if its start and end temperatures are both above 81°C (178°F).  (This is above any mash-out temperature and below the boiling point of water at any inhabited altitude.)  A boil step whose start or end temperature is not given is assumed to be at boiling at that point.  The length of the boil proper is the total `step_time` of its steps.  So:<br> • a first wort addition is `add_to_boil` in a first step (typically `step` 1) that starts at or below 81°C, with no `time` (because it is added at the start of that step -- see `time`)<br> • an ordinary boil addition is `add_to_boil` in the boil proper (typically `step` 2, or with `step` not set), with `time` being how long before the end of the boil proper it is added<br> • a whirlpool or hop stand addition is `add_to_boil` in a later step (typically `step` 3) that ends at or below 81°C.  As with any addition, if `time` is not set then the hops are added at the start of the step, so they steep for the step's `step_time`; and `duration` is only needed if they are removed before the end of the step<br>Readers should identify these steps by their temperatures, as above, rather than relying on the step numbers.

<strong>AdditionSchedule</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| stage | ✅ | Enum:<br>&nbsp;∙ `add_to_mash`<br>&nbsp;∙ `add_to_boil`<br>&nbsp;∙ `add_to_fermentation`<br>&nbsp;∙ `add_to_package` | Differentiates the specific process type when this ingredient addition is used.  Note that `add_to_package` is used, for example, for priming sugar added when beer is bottled. |
| time |  | [Measurement::Time](./Measurement.md#time) | What time during a process step is added, eg a value of 2 days for a dry hop addition would be added 2 days into the fermentation step.  NOTE that, when `stage` is `add_to_boil`, this is time *before* the *end* of the step (or, if no step is specified, of the boil proper -- ie excluding any post-boil steps, as explained above).  For other values of `stage`, this is time *after* the *start* of the step (or of the process if no step is specified).  If none of `time`, `specific_gravity` and `pH` is set, the addition is made at the start of the step (or of the process if no step is specified). |
| duration |  | [Measurement::Time](./Measurement.md#time) | How long an ingredient addition remains, if it is removed before the end of the `stage` in which it was added.  Eg a 2 day duration for a dry hop means to remove it after 2 days.  If this field is not set, the addition is assumed to remain until the end of the `stage`.<br /><br />Note that, for a boil addition, how long it is boiled for is given by `time`, not `duration`: eg a 40 minute boil addition has a `time` of 40 minutes.  So, BeerXML's TIME field (for a hop or misc addition) corresponds to `time` for a boil addition, but to `duration` for a dry hop. |
| specific_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | Used (as an alternative to `time`) to indicate when an addition is added based on a desired specific gravity.  Eg Add dry hop at when SG is 1.018. |
| pH |  | [Measurement::Acidity](./Measurement.md#acidity) | Used (as an alternative to `time`) to indicate when an addition is added based on a desired specific pH.  Eg Add brett when pH is 3.4. |
| step |  | `1 <= x ` | Used to indicate what step this ingredient timing addition is referencing.  Steps are numbered from 1.  Eg A value of 2 for add_to_fermentation would mean to add during the second fermentation step. |

## CultureRecipeAddition

Collects the attributes of each culture ingredient for use in a recipe.  (Unlike in BeerJSON, the `schedule` element is required, as it is for other additions.  For a culture pitched at the start of fermentation, it need only contain `"stage": "add_to_fermentation"`.)

<strong>CultureRecipeAddition</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| culture_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the culture in this addition.  (Obviously the culture in question must be in the "cultures" section of the same dotBeer file.) |
| schedule | ✅ | [AdditionSchedule](#additionschedule) | When the addition is made. |
| amount | ✅ | [Culture::CultureAmount](./Culture.md#cultureamount) | The quantity pitched: by volume for a liquid culture, by mass for a dry one, or by count for whole packets. |
| attenuation |  | [Measurement::PercentageNoMax](./Measurement.md#percentagenomax) | The expected, or measured apparent attenuation for a given culture in a given recipe.  In comparison to attenuation range, this is a single value.  (It can be more than 100% -- see `apparent_attenuation` on Recipe.) |
| times_cultured |  | `0 <= x ` | How many times this culture has been harvested and reused; 0 for fresh product from the producer. |
| cell_count_billions |  | `0 <= x ` | The number of viable cells pitched, in billions. |

## FermentableRecipeAddition

Collects the attributes of each fermentable ingredient for use in a recipe fermentable bill.

<strong>FermentableRecipeAddition</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| fermentable_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the fermentable in this addition.  (Obviously the fermentable in question must be in the "fermentables" section of the same dotBeer file.) |
| schedule | ✅ | [AdditionSchedule](#additionschedule) | When the addition is made. |
| amount | ✅ | [Fermentable::FermentableAmount](./Fermentable.md#fermentableamount) | The quantity added: by mass for a solid, or by volume for a liquid such as a syrup or juice. |

## HopRecipeAddition

Collects the attributes of each hop ingredient for use in a recipe hop bill.

<strong>HopRecipeAddition</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| hop_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the hop in this addition.  (Obviously the hop in question must be in the "hops" section of the same dotBeer file.) |
| schedule | ✅ | [AdditionSchedule](#additionschedule) | When the addition is made. |
| amount | ✅ | [Hop::HopAmount](./Hop.md#hopamount) | The quantity added: by mass for whole, pellet or powdered hops, or by volume for an extract. |

## MiscRecipeAddition

Collects the attributes of each miscellaneous ingredient for use in a recipe.

<strong>MiscRecipeAddition</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| misc_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the misc in this addition.  (Obviously the misc in question must be in the "miscs" section of the same dotBeer file.) |
| schedule | ✅ | [AdditionSchedule](#additionschedule) | When the addition is made. |
| amount | ✅ | [Misc::MiscAmount](./Misc.md#miscamount) | The quantity added: by mass, by volume, or by count for a countable item such as a tablet. |

## Instruction

Descriptive instruction for what to do at a particular point in a recipe.

<strong>Instruction</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string | This is the title of the instruction, eg "Step 2: Heat water". |
| directions | ✅ | string | Detail of what to do at this step, eg "Bring 11.5 L of water to 68.0°C for upcoming infusions". |
| duration |  | [Measurement::Time](./Measurement.md#time) | Where the instruction involves adding something to the boil or holding the mash at a particular temperature, this field tells you how long that should be for.  Eg, if the instruction is "Add 11.5 L water at 68.0 °C to mash to bring it to 68.0 °C. Hold for 50 min." then this field would be `{"unit":"min","value":50}`. |

## BrewLog

Record of a "brewday", ie of an individual brew of a recipe.  Note that:<br> • Fields beginning with "expected_" are values taken from the Recipe (either directly or by calculation)<br> • Fields beginning with "measured_" are supplied by the brewer for this batch -- eg measured OG and FG<br> • Fields beginning with "computed_" are derived from values supplied by the brewer -- eg ABV calculated from measured OG and FG<br>Strictly speaking, "expected_" and "computed_" fields are not needed because they can be derived from other information.  However, we include them because (a) a recipe might have been modified after a brewday and (b) some calculations (eg alcohol by volume) might be done differently by different programs.

<strong>BrewLog</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| batch_number | ✅ | string | The brewer's own unique identifier for this brew.  It can contain numbers and/or letters and/or symbols, so, "number" might seem a bit of a misnomer; nonetheless, it is the standard term for such an identifying code. |
| brew_date | ✅ | [Measurement::Date](./Measurement.md#date) | The date of the "brewday" |
| expected_pre_boil_gravity | ✅ | [Measurement::Gravity](./Measurement.md#gravity) | Expected (planned) pre-boil specific gravity |
| expected_mash_final_temperature | ✅ | [Measurement::Temperature](./Measurement.md#temperature) | Expected (planned) final mash temperature (before any mash out) |
| expected_original_gravity | ✅ | [Measurement::Gravity](./Measurement.md#gravity) | Expected (planned) original (post-boil, pre-fermentation) specific gravity |
| expected_volume_into_fv | ✅ | [Measurement::Volume](./Measurement.md#volume) | Expected (planned) volume of wort into fermentation vessel |
| expected_final_gravity | ✅ | [Measurement::Gravity](./Measurement.md#gravity) | Expected (planned) final (post-fermentation) specific gravity |
| expected_alcohol_by_volume | ✅ | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Expected alcohol by volume based on the recipe OG |
| expected_attenuation | ✅ | [Measurement::PercentageNoMax](./Measurement.md#percentagenomax) | Expected attenuation from the recipe |
| expected_efficiency | ✅ | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Expected brewhouse (ie overall) efficiency from the Recipe, capturing the combined impact of mash conversion, lautering, kettle losses, and transfer |
| expected_boil_off | ✅ | [Measurement::Volume](./Measurement.md#volume) | Expected boil-off based on the equipment profile and the length of the boil |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg stock use instances) to refer to this brew log. |
| ferment_date |  | [Measurement::Date](./Measurement.md#date) | The date fermentation was deemed finished and final gravity readings were taken |
| notes |  | string |  |
| measured_pre_boil_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | Actual (measured) pre-boil specific gravity |
| expected_pre_boil_volume |  | [Measurement::Volume](./Measurement.md#volume) | Expected (planned) volume of wort to be collected from mash into boil kettle |
| measured_pre_boil_volume |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) volume of wort collected from mash into boil kettle |
| expected_strike_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Expected (planned) strike water temperature (ie water temperature immediately prior to adding grains at mash start) |
| measured_strike_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Actual (measured) strike water temperature (ie water temperature immediately prior to adding grains at mash start) |
| measured_mash_final_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Actual (measured) final mash temperature (before any mash out) |
| measured_original_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | Actual (measured) original (post-boil, pre-fermentation) specific gravity |
| measured_post_boil_volume |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) volume of wort in kettle after boil |
| measured_volume_into_fv |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) volume of wort into fermentation vessel |
| measured_pitch_temperature |  | [Measurement::Temperature](./Measurement.md#temperature) | Actual (measured) temperature of wort when yeast is pitched |
| measured_final_gravity |  | [Measurement::Gravity](./Measurement.md#gravity) | Actual (measured) final (post-fermentation) specific gravity |
| measured_final_volume |  | [Measurement::Volume](./Measurement.md#volume) | Actual (measured) final (post-fermentation) volume |
| computed_alcohol_by_volume |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Actual alcohol by volume based on "original" and "final" gravity readings |
| computed_attenuation |  | [Measurement::PercentageNoMax](./Measurement.md#percentagenomax) | Actual attenuation based on gravity readings |
| computed_efficiency |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Actual brewhouse (ie overall) efficiency based on gravity readings |
| computed_pre_boil_efficiency |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Actual pre-boil (aka "into boil kettle") efficiency, measuring the percentage of total available sugars that made it into the kettle |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-23 at 12:55:01+0200.
