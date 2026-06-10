# Style

A beer style may be from the BJCP style guide, Australian, UK or local style guides.  Generally a recipe is designed to one style.

<strong>Style</strong> is a JSON object with all properties from [StyleBase](#stylebase) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| original_gravity |  | [Measurement::RangeOfDensity](./Measurement.md#rangeofdensity) | The range of acceptable original gravity for the style. |
| final_gravity |  | [Measurement::RangeOfDensity](./Measurement.md#rangeofdensity) | The range of acceptable final gravity for the style. |
| international_bitterness_units |  | [Measurement::RangeOfBitterness](./Measurement.md#rangeofbitterness) | The range of bitterness for this style. |
| color |  | [Measurement::RangeOfColor](./Measurement.md#rangeofcolor) | The range of color for this beer style. |
| carbonation |  | [Measurement::RangeOfCarbonation](./Measurement.md#rangeofcarbonation) | Range of carbonation for this beer style. |
| alcohol_by_volume |  | [Measurement::RangeOfPercentage](./Measurement.md#rangeofpercentage) | The range of alcohol by volume for this beer style. |
| notes |  | string | Description of the style, history |
| aroma |  | string | Aroma profile for this style. |
| appearance |  | string |  |
| flavor |  | string | Flavor profile for this style. |
| mouthfeel |  | string |  |
| overall_impression |  | string |  |
| ingredients |  | string | Suggested ingredients for this style |
| examples |  | string | Example beers of this style. |


---

# Component Types

## StyleBase

The descriptive base type for both style guideline records, and recipe style provisions. Provides unique properties to identify individual styles

<strong>StyleBase</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string | Name of the style profile – usually this is the specific name of the style – for example “Scottish Wee Heavy Ale” and not the Category which in this case might be “Scottish Ale” |
| category | ✅ | string | Category that this style belongs to – usually associated with a group of styles such as “English Ales” or “American Lagers”. |
| style_guide | ✅ | string | The name of the style guide that this particular style or category belongs to. For example “BJCP” might denote the BJCP style guide, and “AHA” would be used for the AHA style guide. |
| style_type | ✅ | Enum:<br>&nbsp;∙ `beer`<br>&nbsp;∙ `cider`<br>&nbsp;∙ `kombucha`<br>&nbsp;∙ `mead`<br>&nbsp;∙ `other`<br>&nbsp;∙ `soda`<br>&nbsp;∙ `wine` | Defines the type of beverage associated with this category. |
| category_number |  | integer | Number or identifier associated with this style category. For example in the BJCP style guide, the “American Lager” category has a category number of “1”. |
| style_letter |  |  matching regular expression [`[A-Z ]`](https://regex101.com/?regex=%5BA-Z+%5D) | The specific subcategory letter associated with this particular style. For example in the BJCP style guide, an American Standard Lager would be style letter “A” under the main category.  Letters should be upper case. |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.2.0) on 2026-06-10 at 09:03:35+0200.
