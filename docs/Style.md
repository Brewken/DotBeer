# Style

The full definition of a Style categorization

<strong>Style</strong> is a JSON object with all properties from [StyleBase](#stylebase) as well as these additional ones:

| Property | Required? | Type |
| -------- | -------- | --------------- |
| original_gravity |  | [Measurement::RangeOfDensity](./Measurement.md#rangeofdensity) |
| final_gravity |  | [Measurement::RangeOfDensity](./Measurement.md#rangeofdensity) |
| international_bitterness_units |  | [Measurement::RangeOfBitterness](./Measurement.md#rangeofbitterness) |
| color |  | [Measurement::RangeOfColor](./Measurement.md#rangeofcolor) |
| carbonation |  | [Measurement::RangeOfCarbonation](./Measurement.md#rangeofcarbonation) |
| alcohol_by_volume |  | [Measurement::RangeOfPercentage](./Measurement.md#rangeofpercentage) |
| notes |  | string |
| aroma |  | string |
| appearance |  | string |
| flavor |  | string |
| mouthfeel |  | string |
| overall_impression |  | string |
| ingredients |  | string |
| examples |  | string |


---

# Definitions

## StyleBase

The descriptive base type for both style guideline records, and recipe style provisions. Provides unique properties to identify individual styles

<strong>StyleBase</strong> is a JSON object with the following properties:

| Property | Required? | Type |
| -------- | -------- | --------------- |
| name | ✅ | string |
| category | ✅ | string |
| style_guide | ✅ | string |
| style_type | ✅ | Enum:<br>&nbsp;∙ `beer`<br>&nbsp;∙ `cider`<br>&nbsp;∙ `kombucha`<br>&nbsp;∙ `mead`<br>&nbsp;∙ `other`<br>&nbsp;∙ `soda`<br>&nbsp;∙ `wine` |
| category_number |  | integer |
| style_letter |  |  matching regular expression [`[A-Z ]`](https://regex101.com/?regex=%5BA-Z+%5D) |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
