# Measurement

'Measurement' is not a type itself, but a subschema holding various types of measurement, and ranges thereof.

In principle, we could have sub-groupings such as "physical quantities" (volume, mass, acidity, etc), "non-physical quantities" (percentage, count, date, etc).  However, this adds complexity to the schema for little gain, because there is nowhere else in the schema where we would rely on such groupings.  So, instead, we keep a flat hierarchy.

In several cases, there is only one possible unit (eg acidity, percentage, count), so it would be possible to omit units altogether.  However, in common with BeerJSON, we retain them for a couple of reasons.  Firstly, it makes the serialisation easier to understand for human readers.  Secondly, it makes things more extendable: eg, if we decided at a future date we would like to support "percentage points" in addition to "percentages", then it's a smaller change to add them.

For Ranges, note that we do not force the same units for lower and upper bounds.  This is partly because it would complicate the schema for only small gain, and partly because it's conceivable that you want different units on min and max (eg if you had a mass range you might want min in grams and max in kilograms).


---

# Component Types

## Acidity



<strong>Acidity</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `pH` |  |
| value | ✅ | `-1.1 <= x <= 15.0` | The minimum and maximum pH values here come from the table on https://fr.wikipedia.org/wiki/Potentiel_hydrog%C3%A8ne.  In practice, a smaller range would probably suffice. |

## Bitterness



<strong>Bitterness</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `IBUs` |
| value | ✅ | `0 <= x ` |

## Carbonation



<strong>Carbonation</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `vols`<br>&nbsp;∙ `g/l` |
| value | ✅ | `0 <= x ` |

## Color

Supports both grain color properties, such as Lovibond, and wort color properties such as SRM and EBC.

<strong>Color</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `EBC`<br>&nbsp;∙ `Lovi`<br>&nbsp;∙ `SRM` | `EBC` is European Brewing Convention system of color measurement<br>`Lovi` is Lovibond<br>`SRM` is Standard Reference Method color measurement system |
| value | ✅ | `0 <= x ` |  |

## Count

Used where unitless amounts are required, such as 1 apple, or 1 yeast packet.  Note that this _is_ allowed to be fractional because you might want to add 1½ cinnamon sticks or 2.5 packets of yeast.

<strong>Count</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `1`<br>&nbsp;∙ `unit`<br>&nbsp;∙ `each`<br>&nbsp;∙ `dimensionless`<br>&nbsp;∙ `pkg` |
| value | ✅ | `0 <= x ` |

## Date

To avoid ambiguity, dates are always stored in ISO 8601 format.  The two possibilities here are with and without time of day.

<strong>Date</strong> is a ``string``  matching regular expression [`^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?(Z\|[+-]\d{2}:\d{2})?)?$`](https://regex101.com/?regex=%5E%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D%28T%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7D%28%5C.%5Cd%2B%29%3F%28Z%7C%5B%2B-%5D%5Cd%7B2%7D%3A%5Cd%7B2%7D%29%3F%29%3F%24)

## Gravity

In brewing, "gravity" is a shorthand for "specific gravity".  Typically, brewers measure relative gravity (aka specific gravity) to gauge percent of sugar content (ie Plato and Brix).

<strong>Gravity</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `sg`<br>&nbsp;∙ `plato`<br>&nbsp;∙ `brix` | `sg` is specific gravity<br>`plato` is degrees Plato (°P)<br>`brix` is degrees Brix (°Bx) |
| value | ✅ | `0 <= x ` |  |

## DiastaticPower

Diastatic power is a measurement of malted grains enzymatic content. A value of 35 Lintner is needed to self convert, while a value of 100 or more is desirable for base malts.

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
| unit | ✅ | Enum:<br>&nbsp;∙ `mg`<br>&nbsp;∙ `g`<br>&nbsp;∙ `kg`<br>&nbsp;∙ `lb`<br>&nbsp;∙ `oz` | `mg` is milligrams<br>`g` is grams<br>`kg` is kilograms<br>`lb` is pounds (imperial and US customary)<br>`oz` is ounces (imperial and US customary) |
| value | ✅ | `0 <= x ` |  |

## MassFractionOrConcentration

Strictly speaking, mass concentration (eg mg/l) is different from mass fraction (eg ppm, ppb) but, in the context of brewing, it is usually approximately true that 1 mg/L mass concentration = 1 parts per million (ppm) mass fraction.

<strong>MassFractionOrConcentration</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `ppm`<br>&nbsp;∙ `ppb`<br>&nbsp;∙ `mg/l` | `ppm` is parts per million<br>`ppb` is parts per billion<br>`mg/l` is milligrams per liter |
| value | ✅ | `0 <= x ` |  |

## PercentageNoMax

PercentageNoMax, aka, "no max percentage" is a percentage that can be more than 100% (but cannot be less than 0%)

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

## Pressure



<strong>Pressure</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `kPa`<br>&nbsp;∙ `psi`<br>&nbsp;∙ `bar` | `kPa` is kilopascals<br>`psi` is pounds per square inch<br>`bar` is bar (where 1 bar = 100 kPa) |
| value | ✅ | `0 <= x ` |  |

## SpecificHeatCapacity

The amount of heat that must be added to one unit of mass of the substance in order to cause an increase of one unit in temperature.

<strong>SpecificHeatCapacity</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `Cal/(g C)`<br>&nbsp;∙ `J/(kg K)`<br>&nbsp;∙ `BTU/(lb F)` |
| value | ✅ | `0 <= x ` |

## SpecificVolume

Specific volume is the reciprocal of Gravity, commonly used for mash thickness.

<strong>SpecificVolume</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | --------- | ---- |
| unit | ✅ | Enum:<br>&nbsp;∙ `qt/lb`<br>&nbsp;∙ `gal/lb`<br>&nbsp;∙ `gal/oz`<br>&nbsp;∙ `l/g`<br>&nbsp;∙ `l/kg`<br>&nbsp;∙ `floz/oz`<br>&nbsp;∙ `m^3/kg`<br>&nbsp;∙ `ft^3/lb` |
| value | ✅ | `0 <= x ` |

## Temperature



<strong>Temperature</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| unit | ✅ | Enum:<br>&nbsp;∙ `C`<br>&nbsp;∙ `F` | `C` is degrees Celsius (°C)<br>`F` is degrees Fahrenheit (°F) |
| value | ✅ | `0 <= x ` |  |

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
| unit | ✅ | Enum:<br>&nbsp;∙ `ml`<br>&nbsp;∙ `l`<br>&nbsp;∙ `tsp`<br>&nbsp;∙ `tbsp`<br>&nbsp;∙ `floz`<br>&nbsp;∙ `cup`<br>&nbsp;∙ `pt`<br>&nbsp;∙ `qt`<br>&nbsp;∙ `gal`<br>&nbsp;∙ `bbl`<br>&nbsp;∙ `itsp`<br>&nbsp;∙ `itbsp`<br>&nbsp;∙ `ifloz`<br>&nbsp;∙ `icup`<br>&nbsp;∙ `ipt`<br>&nbsp;∙ `iqt`<br>&nbsp;∙ `igal`<br>&nbsp;∙ `ibbl` | `ml` is milliliters (Metric/SI)<br>`l` is liters (Metric/SI)<br>`tsp` is US teaspoons<br>`tbsp` is US tablespoons<br>`floz` is US fluid ounces<br>`cup` is US cups<br>`pt` is US pints (liquid)<br>`qt` is US quarts (liquid)<br>`gal` is US gallons (liquid)<br>`bbl` is US barrels (liquid)<br>`itsp` is Imperial teaspoons<br>`itbsp` is Imperial tablespoons<br>`ifloz` is Imperial fluid ounces<br>`icup` is Imperial cups<br>`ipt` is Imperial pints (liquid)<br>`iqt` is Imperial quarts (liquid)<br>`igal` is Imperial gallons (liquid)<br>`ibbl` is Imperial barrels (liquid) |
| value | ✅ | `0 <= x ` |  |

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

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (vNone) on 2026-10-07 at 21:03:19+0200.
