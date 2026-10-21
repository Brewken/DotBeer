# Style

A beer style may be from the BJCP style guide, Australian, UK or local style guides.  Generally a recipe is designed to one style.

Range fields (`original_gravity`, `final_gravity`, `ibu`, `color`, `alcohol_by_volume`, `carbonation`) should be interpreted as typical range for the style, as given in the style guide (eg the “Vital Statistics” in the BJCP guidelines).  These are guidelines rather than hard limits: a beer slightly outside a range may still be a good example of the style.

<strong>Style</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string | Name of the style profile – usually this is the specific name of the style – for example “Scottish Wee Heavy Ale” and not the Category which in this case might be “Scottish Ale” |
| category | ✅ | string | Category that this style belongs to – usually associated with a group of styles such as “English Ales” or “American Lagers”. |
| style_guide | ✅ | string | Who published the guidelines, ideally with the edition, eg “BJCP 2021” or “BA 2024”.  Including the edition matters because category numbers and style definitions change between editions. |
| style_type | ✅ | Enum:<br>&nbsp;∙ `beer`<br>&nbsp;∙ `cider`<br>&nbsp;∙ `kombucha`<br>&nbsp;∙ `mead`<br>&nbsp;∙ `other`<br>&nbsp;∙ `soda`<br>&nbsp;∙ `wine` | Defines the type of beverage associated with this category. |
| category_number |  | string | Number or identifier associated with this style category. For example in the BJCP 2021 style guide, “Czech Premium Pale Lager” is category number “3”, style letter “B”, ie “3B”.<br /><br />Note that, despite the name, this needs to be a string rather than, say, an integer, because it can contain letters.  Eg BJCP mead and cider categories are M1–M4 and C1–C2. |
| style_letter |  |  matching regular expression [`^[A-Z]$`](https://regex101.com/?regex=%5E%5BA-Z%5D%24) | The specific subcategory letter associated with this particular style. For example in the BJCP 2021 style guide, an American Lager would be style letter “B” under the main category (1 = Standard American Beer).  Letters should be upper case. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this style. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Style object. |
| original_gravity |  | [Measurement::RangeOfGravity](./Measurement.md#rangeofgravity) |  |
| final_gravity |  | [Measurement::RangeOfGravity](./Measurement.md#rangeofgravity) |  |
| ibu |  | [Measurement::RangeOfBitterness](./Measurement.md#rangeofbitterness) |  |
| color |  | [Measurement::RangeOfColor](./Measurement.md#rangeofcolor) |  |
| carbonation |  | [Measurement::RangeOfCarbonation](./Measurement.md#rangeofcarbonation) | Note that, in contrast with the other range fields, the BJCP guidelines don’t give carbonation figures, so this usually comes from other sources. |
| alcohol_by_volume |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) |  |
| notes |  | string | Anything else about the style not covered by the other fields, eg its history, or comments on what is and isn’t acceptable.  (In the BJCP guidelines, this is typically the “Comments” and “History” sections.) |
| aroma |  | string | The aroma expected in a good example of the style: malt, hop, fermentation and other characteristics, and how they balance. |
| appearance |  | string | Expected colour, clarity, and head (colour, texture and retention). |
| flavor |  | string | Expected flavour profile: malt, hop bitterness and flavour, fermentation character, balance and finish. |
| mouthfeel |  | string | Expected body, carbonation, alcohol warmth, creaminess, astringency and other sensations on the palate. |
| overall_impression |  | string | A short summary of the style’s character, ie what distinguishes it at a glance.  Corresponds to the “Overall Impression” section of the BJCP guidelines. |
| ingredients |  | string | The ingredients characteristic of the style, eg particular malts, hop varieties, yeast strains or water profile. Corresponds to “Characteristic Ingredients” in the BJCP guidelines. |
| examples |  | string | Commercial beers that are good examples of the style. |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-21 at 21:58:05+0200.
