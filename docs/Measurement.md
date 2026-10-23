# Measurement

'Measurement' is not a type itself, but a subschema holding various types of measurement, and ranges thereof.

In principle, we could have sub-groupings such as "physical quantities" (volume, mass, acidity, etc), "non-physical quantities" (percentage, count, date, etc).  However, this adds complexity to the schema for little gain, because there is nowhere else in the schema where we would rely on such groupings.  So, instead, we keep a flat hierarchy.

In several cases, there is only one possible unit (eg acidity, percentage, count), so it would be possible to omit units altogether.  However, in common with BeerJSON, we retain them for a couple of reasons.  Firstly, it makes the serialisation easier to understand for human readers.  Secondly, it makes things more extendable: eg, if we decided at a future date we would like to support "percentage points" in addition to "percentages", then it's a smaller change to add them.

For Ranges, note that we do not force the same units for lower and upper bounds.  This is partly because it would complicate the schema for only small gain, and partly because it's conceivable that you want different units on min and max (eg if you had a mass range you might want min in grams and max in kilograms).


---

# Component Types

## Acidity



<strong>Acidity</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `pH` |
| value | ✅ | `-1.1 <= x <= 15.0` |

## Bitterness



<strong>Bitterness</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `IBUs` |
| value | ✅ | `0 <= x ` |

## Carbonation



<strong>Carbonation</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `vols`<br>&nbsp;∙ `g/l` | `vols` = volumes of CO₂, ≈ 1.96 g/L each. |
| value | ✅ | `0 <= x ` |  |

## Color

Supports both grain color properties, such as Lovibond, and wort color properties such as SRM and EBC.

<strong>Color</strong> is a JSON object with the following properties:

| Property | Required? | Type | Conditional? | Description |
| -------- | --------- | ---- | ------------ | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `EBC`<br>&nbsp;∙ `Lovi`<br>&nbsp;∙ `SRM` |  | `EBC` is European Brewing Convention system of color measurement<br>`Lovi` is Lovibond<br>`SRM` is Standard Reference Method color measurement system |
| value | ✅ | number |  |  |
| value |  | None | **If** unit = Lovi |  |
| value |  | None | **If** unit = SRM |  |
| value |  | None | **If** unit = EBC |  |

## Count

Used where unitless amounts are required, such as 1 apple, or 1 yeast packet.  Note that this _is_ allowed to be fractional because you might want to add 1½ cinnamon sticks or 2.5 packets of yeast.  Note too, that this is only used in cases where things might be measured in multiple ways.  Eg a Misc can be measured by Volume, Mass or Count (depending on what it is).  In other places that use a count, eg CultureRecipeAddition.times_cultured, we just use a non-negative integer.

<strong>Count</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `count` |
| value | ✅ | `0 <= x ` |

## CurrencyAmount

An amount of a currency, eg $1.23 or €3.45.

<strong>CurrencyAmount</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| iso_alphabetic_code | ✅ |  matching regular expression [`^[A-WYZ][A-Z]{2}$`](https://regex101.com/?regex=%5E%5BA-WYZ%5D%5BA-Z%5D%7B2%7D%24) | The three-letter ISO 4217 alphabetic code for this currency, eg AUD for Australian Dollars, CAD for Canadian Dollars, USD for US Dollars.<br /><br />Note that codes beginning with X are not supported. |
| amount | ✅ | `0 <= x ` |  |

## Date

A calendar date in ISO 8601 / RFC 3339 format, ie YYYY-MM-DD.

<strong>Date</strong> is a ``string``  matching regular expression [`^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])$`](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%280%5B1-9%5D%7C1%5B0-2%5D%29-%280%5B1-9%5D%7C%5B12%5D%5B0-9%5D%7C3%5B01%5D%29%24)

## DateTimeOffset

A date and time of day in ISO 8601 / RFC 3339 format, ie YYYY-MM-DDThh:mm:ss, optionally with fractional seconds, and always with a timezone: either `Z` for UTC or an offset such as `+02:00`.  Eg 2026-10-14T09:08:00+02:00.

<strong>DateTimeOffset</strong> is a ``string``  matching regular expression [`^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])T([01][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?(Z\|[+-]([01][0-9]\|2[0-3]):[0-5][0-9])$`](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%280%5B1-9%5D%7C1%5B0-2%5D%29-%280%5B1-9%5D%7C%5B12%5D%5B0-9%5D%7C3%5B01%5D%29T%28%5B01%5D%5B0-9%5D%7C2%5B0-3%5D%29%3A%5B0-5%5D%5B0-9%5D%3A%28%5B0-5%5D%5B0-9%5D%7C60%29%28%5B.%5D%5B0-9%5D%2B%29%3F%28Z%7C%5B%2B-%5D%28%5B01%5D%5B0-9%5D%7C2%5B0-3%5D%29%3A%5B0-5%5D%5B0-9%5D%29%24)

## DateOrDateTimeLocal

Either a calendar date (YYYY-MM-DD) or a date and time of day (YYYY-MM-DDThh:mm:ss, optionally with fractional seconds), in ISO 8601 / RFC 3339 format.  A time may be followed by a timezone (`Z` for UTC or an offset such as `+02:00`); if it is not, it is a local time.  Eg 2026-10-14, 2026-10-14T09:08:00 or 2026-10-14T09:08:00+02:00.

<strong>DateOrDateTimeLocal</strong> is a ``string``  matching regular expression [`^[0-9]{4}-(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])(T([01][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)([.][0-9]+)?(Z\|[+-]([01][0-9]\|2[0-3]):[0-5][0-9])?)?$`](https://regex101.com/?regex=%5E%5B0-9%5D%7B4%7D-%280%5B1-9%5D%7C1%5B0-2%5D%29-%280%5B1-9%5D%7C%5B12%5D%5B0-9%5D%7C3%5B01%5D%29%28T%28%5B01%5D%5B0-9%5D%7C2%5B0-3%5D%29%3A%5B0-5%5D%5B0-9%5D%3A%28%5B0-5%5D%5B0-9%5D%7C60%29%28%5B.%5D%5B0-9%5D%2B%29%3F%28Z%7C%5B%2B-%5D%28%5B01%5D%5B0-9%5D%7C2%5B0-3%5D%29%3A%5B0-5%5D%5B0-9%5D%29%3F%29%3F%24)

## EnergyPerVolume

Energy per volume is used in nutritional labelling.
`kcal/l` is kilocalories per liter<br>`kcal/50cl` is kilocalories per 50 centiliters<br>`kcal/33cl` is kilocalories per 33 centiliters<br>`kcal/25cl` is kilocalories per 25 centiliters<br>`kcal/100ml` is kilocalories per 100 milliliters*<br>`kcal/pt` is kilocalories per US pint (16 US fluid ounces)<br>`kcal/12floz` is kilocalories per 12 US fluid ounces<br>`kcal/ipt` is kilocalories per imperial pint<br>`kJ/100ml` is kilojoules per 100 milliliters*<br>Those marked * are EU standards for nutritional labelling.

<strong>EnergyPerVolume</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `kcal/l`<br>&nbsp;∙ `kcal/50cl`<br>&nbsp;∙ `kcal/33cl`<br>&nbsp;∙ `kcal/25cl`<br>&nbsp;∙ `kcal/100ml`<br>&nbsp;∙ `kcal/pt`<br>&nbsp;∙ `kcal/12floz`<br>&nbsp;∙ `kcal/ipt`<br>&nbsp;∙ `kJ/100ml` |
| value | ✅ | `0 <= x ` |

## Gravity

In brewing, "gravity" is a shorthand for "specific gravity".  Typically, brewers measure relative gravity (aka specific gravity) to gauge percent of sugar content (ie Plato and Brix).

We assume that brewers don't need "specific gravity" below 0.900 SG (about -30°P/°Bx).  At the other end, because degrees Plato and Brix are percentages of sugar by weight, they cannot exceed 100, which corresponds to about 1.6 SG (the density of sucrose itself), so these are the maximums.

<strong>Gravity</strong> is a JSON object with the following properties:

| Property | Required? | Type | Conditional? | Description |
| -------- | --------- | ---- | ------------ | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `sg`<br>&nbsp;∙ `plato`<br>&nbsp;∙ `brix` |  | `sg` is specific gravity<br>`plato` is degrees Plato (°P)<br>`brix` is degrees Brix (°Bx) |
| value | ✅ | number |  |  |
| value |  | None | **If** unit = sg |  |
| value |  | None | **If NOT** unit = sg |  |

## DiastaticPower

Diastatic power is a measurement of malted grains enzymatic content.  More specifically, it is the total activity of malt enzymes that hydrolyze starch to fermentable sugars.  The starch-degrading enzymes contributing to this process are alpha-amylase, beta-amylase, limit dextrinase, and alpha-glucosidase.  The driving force for DP appears to be beta amylase, which usually correlates better with DP than the other starch-degrading enzymes and has the highest activity of all starch-degrading enzymes in malt.

`WK` = Windisch-Kolbach, and °WK = 3.5 × °L − 16.

<strong>DiastaticPower</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `Lintner`<br>&nbsp;∙ `WK` |
| value | ✅ | `0 <= x ` |

## Length



<strong>Length</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `mm`<br>&nbsp;∙ `cm`<br>&nbsp;∙ `m`<br>&nbsp;∙ `in`<br>&nbsp;∙ `ft` |
| value | ✅ | `0 <= x ` |

## Mass



<strong>Mass</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `mg`<br>&nbsp;∙ `g`<br>&nbsp;∙ `kg`<br>&nbsp;∙ `lb`<br>&nbsp;∙ `oz` | `mg` is milligrams<br>`g` is grams<br>`kg` is kilograms<br>`lb` is pounds (imperial and US customary, which are the same) = 453.59237 g exactly<br>`oz` is ounces (imperial and US customary, which are the same) = 1/16 lb ≈ 28.35 g.  (NB these are avoirdupois ounces, not troy ounces.) |
| value | ✅ | `0 <= x ` |  |

## MassFractionOrConcentration

Strictly speaking, mass concentration (eg mg/l) is different from mass fraction (eg ppm, ppb) but, in the context of brewing, it is usually approximately true that 1 mg/L mass concentration = 1 parts per million (ppm) mass fraction.

<strong>MassFractionOrConcentration</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `ppm`<br>&nbsp;∙ `ppb`<br>&nbsp;∙ `mg/l` | `ppm` is parts per million<br>`ppb` is parts per billion<br>`mg/l` is milligrams per liter |
| value | ✅ | `0 <= x ` |  |

## PercentageNoMax

PercentageNoMax, aka, "no max percentage" is a percentage that can be more than 100% (but cannot be less than 0%).

NOTE: This is not currently used, but is reserved for future use.

<strong>PercentageNoMax</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `%` |
| value | ✅ | `0 <= x ` |

## PercentageSimple

PercentageSimple, aka, "simple percentage" is a percentage where the value is no less than 0% and no greater than 100%

<strong>PercentageSimple</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `%` |
| value | ✅ | `0 <= x <= 100` |

## SpecificHeatCapacity

The amount of heat that must be added to one unit of mass of the substance in order to cause an increase of one unit in temperature.<br>`c/g·C` is calories per Celsius per gram (and also kilocalories per degree Celsius per kilogram)<br>`J/kg·K` is joules per Kelvin per kilogram<br>`BTU/lb·F` is BTU per Fahrenheit per pound<br>Although SI units are "joules per kelvin per kilogram" (which is the same as "joules per degree Celsius per kilogram"), historically a measurement involving calories instead of joules was used in chemistry, nutrition and brewing.  There are two types of calorie: the "small calorie" (or "gram-calorie", "cal") = 4.184 J; and the "grand calorie" (aka "kilocalorie", "kcal" or "Cal") = 1000 small calories = 4184 J.  However, the specific heat measurement using "cal" ("calories per degree Celsius per gram") is the same as that for "Cal" ("kilocalories per degree Celsius per kilogram"): 1 cal / (°C × g) = 1 Cal / (°C × kg) = 4184 J / (K × kg) = the specific heat capacity of liquid water.  Note too that, because a British Thermal Unit (BTU) is defined as "the amount of heat required to raise the temperature of one pound of water by one degree Fahrenheit", we have 1 BTU/lb·F = 1 c/g·C.

<strong>SpecificHeatCapacity</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `c/g·C`<br>&nbsp;∙ `J/kg·K`<br>&nbsp;∙ `BTU/lb·F` |
| value | ✅ | `0 <= x ` |

## Temperature

`C` is degrees Celsius (°C)<br>`F` is degrees Fahrenheit (°F).  We assume that brewers never need temperatures below -30°C (-22°F) or above 150°C (302°F).

<strong>Temperature</strong> is a JSON object with the following properties:

| Property | Required? | Type | Conditional? |
| -------- | --------- | ---- | ------------ |
| unit | ✅ | Enum:<br>&nbsp;∙ `C`<br>&nbsp;∙ `F` |  |
| value | ✅ | number |  |
| value |  | None | **If** unit = C |
| value |  | None | **If NOT** unit = C |

## Time

Note this is NOT dates or times of day but length-of-time or elapsed time, eg duration of a mash step, or how long after the start of the boil to add something.

<strong>Time</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `sec`<br>&nbsp;∙ `min`<br>&nbsp;∙ `hr`<br>&nbsp;∙ `day`<br>&nbsp;∙ `week` | `sec` is seconds<br>`min` is minutes<br>`hr` is hours<br>`day` is days<br>`week` is weeks<br> |
| value | ✅ | `0 <= x ` |  |

## Viscosity

Viscosity of fluids

<strong>Viscosity</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `cP`<br>&nbsp;∙ `mPa-s` |
| value | ✅ | `0 <= x ` |

## Volume



<strong>Volume</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `ml`<br>&nbsp;∙ `l`<br>&nbsp;∙ `tsp`<br>&nbsp;∙ `tbsp`<br>&nbsp;∙ `floz`<br>&nbsp;∙ `cup`<br>&nbsp;∙ `pt`<br>&nbsp;∙ `qt`<br>&nbsp;∙ `gal`<br>&nbsp;∙ `bbl`<br>&nbsp;∙ `itsp`<br>&nbsp;∙ `itbsp`<br>&nbsp;∙ `ifloz`<br>&nbsp;∙ `icup`<br>&nbsp;∙ `ipt`<br>&nbsp;∙ `iqt`<br>&nbsp;∙ `igal`<br>&nbsp;∙ `ibbl` | `ml` is milliliters (Metric/SI)<br>`l` is liters (Metric/SI)<br>`tsp` is US teaspoons = ⅙ US fl oz ≈ 4.929 ml<br>`tbsp` is US tablespoons = 3 US tsp = ½ US fl oz ≈ 14.79 ml<br>`floz` is US fluid ounces = ⅛ US cup ≈ 29.57 ml<br>`cup` is US customary cups = 8 US fl oz ≈ 236.6 ml (NB not the 240 ml "legal" cup used for US nutrition labelling)<br>`pt` is US pints (liquid) = 16 US fl oz ≈ 473.2 ml<br>`qt` is US quarts (liquid) = 2 US pt ≈ 946.4 ml<br>`gal` is US gallons (liquid) = 4 US qt = 3.785411784 l exactly<br>`bbl` is US beer barrels = 31 US gal ≈ 117.3 l (NB not the 31.5 US gal barrel used for other liquids, nor the 42 US gal oil barrel)<br>`itsp` is Imperial teaspoons = 1 Imperial fluid drachm = ⅛ Imperial fl oz ≈ 3.552 ml<br>`itbsp` is Imperial tablespoons = 4 Imperial tsp = ½ Imperial fl oz ≈ 14.21 ml (NB 4 teaspoons to the tablespoon, unlike in the US)<br>`ifloz` is Imperial fluid ounces = 1/160 Imperial gal ≈ 28.41 ml<br>`icup` is Imperial cups = 10 Imperial fl oz = ½ Imperial pt ≈ 284.1 ml<br>`ipt` is Imperial pints (liquid) = 20 Imperial fl oz ≈ 568.3 ml<br>`iqt` is Imperial quarts (liquid) = 2 Imperial pt ≈ 1.137 l<br>`igal` is Imperial gallons (liquid) = 4 Imperial qt = 4.54609 l exactly<br>`ibbl` is Imperial beer barrels = 36 Imperial gal ≈ 163.7 l<br><br /><br />Where a unit has more than one definition in common use, these are the ones that dotBeer uses.  (The traditional Imperial spoons here are rarely used in modern British recipes, which mostly use metric spoons of 5 ml and 15 ml -- in which case, it is clearer to record amounts in `ml`.) |
| value | ✅ | `0 <= x ` |  |

## VolumePerMass

For a single substance, volume-per-mass is the substance's "specific volume" (see https://en.wikipedia.org/wiki/Specific_volume), which is the reciprocal of its density.  However, in brewing, volume-per-mass is mostly used for ratios between two different things -- eg mash thickness (volume of water per mass of grain) or grain absorption rate (volume of water absorbed per mass of grain).  In such cases, it would be inaccurate to refer to "specific volume".

<strong>VolumePerMass</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `qt/lb`<br>&nbsp;∙ `gal/lb`<br>&nbsp;∙ `gal/oz`<br>&nbsp;∙ `l/g`<br>&nbsp;∙ `l/kg`<br>&nbsp;∙ `floz/oz`<br>&nbsp;∙ `m^3/kg`<br>&nbsp;∙ `ft^3/lb` |
| value | ✅ | `0 <= x ` |

## RangeOfBitterness



<strong>RangeOfBitterness</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| minimum | ✅ | [Bitterness](#bitterness) |
| maximum | ✅ | [Bitterness](#bitterness) |

## RangeOfCarbonation



<strong>RangeOfCarbonation</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| minimum | ✅ | [Carbonation](#carbonation) |
| maximum | ✅ | [Carbonation](#carbonation) |

## RangeOfTemperature



<strong>RangeOfTemperature</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| minimum | ✅ | [Temperature](#temperature) |
| maximum | ✅ | [Temperature](#temperature) |

## RangeOfColor



<strong>RangeOfColor</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| minimum | ✅ | [Color](#color) |
| maximum | ✅ | [Color](#color) |

## RangeOfGravity



<strong>RangeOfGravity</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| minimum | ✅ | [Gravity](#gravity) |
| maximum | ✅ | [Gravity](#gravity) |

## RangeOfPercentageSimple



<strong>RangeOfPercentageSimple</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| minimum | ✅ | [PercentageSimple](#percentagesimple) |
| maximum | ✅ | [PercentageSimple](#percentagesimple) |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-23 at 08:16:31+0200.
