# Hop

Full definition of a hop variety.

<strong>Hop</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| alpha_acid | ✅ | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The actual alpha acid content of the specific year's harvest (and batch) of this type of hop. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this hop. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Hop object. |
| producer |  | string |  |
| product_id |  | string |  |
| origin |  | string | Country of origin for the hop variety |
| year |  | string | Year of harvest.  (Note that this is intentionally not a number, as, for one thing, years are not generally formatted in the same way as numbers.) |
| form |  | Enum:<br>&nbsp;∙ `extract`<br>&nbsp;∙ `leaf`<br>&nbsp;∙ `leaf (wet)`<br>&nbsp;∙ `pellet`<br>&nbsp;∙ `powder`<br>&nbsp;∙ `plug` |  |
| alpha_acid_range |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) | The typical range of alpha acid for this type of hop. |
| beta_acid |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The actual beta acid content of the specific year's harvest (and batch) of this type of hop. |
| beta_acid_range |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) | The typical range of beta acid for this type of hop. |
| hop_type |  | Enum:<br>&nbsp;∙ `aroma`<br>&nbsp;∙ `bittering`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `aroma/bittering`<br>&nbsp;∙ `bittering/flavor`<br>&nbsp;∙ `aroma/flavor`<br>&nbsp;∙ `aroma/bittering/flavor` |  |
| notes |  | string |  |
| six_month_alpha_loss |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The percentage of hop alpha lost in 6 months of storage.<br /><br />Note that this is percentage and not percentage points.  So, eg, if a hop starts out with 4.0% `alpha_acid` and has 25% `six_month_alpha_loss`, then we would expect its alpha acid to be 3.0% after six months in storage. |
| substitutes |  | string | Alternate hop varieties that can be used in place of this hop variety |
| cohumulone |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Cohumulone as a percentage of total hop alpha acids.  Per (English translation of) https://fr.wikipedia.org/wiki/Cohumulone: "Cohumulone is one of the three hop-derived alpha acids that provide beer with most of its bitterness.  Some brewers believe that hop varieties with a high cohumulone content produce a harsher bitterness.  Cohumulone generally accounts for between 20% and 50% of a hop’s alpha acid content.  Cohumulone, like other known alpha acids (the main ones being humulone and adhumulone), is produced by the breakdown of lupulin (derived from hops).   However, it has greater polarity and better solubility in water than other alpha acids.  In water, its isomerization produces two compounds: cis-isocohumulone and trans-isocohumulone, which appear to impart a harsher bitterness than that of isohumulones." |
| oil_content |  | [OilContent](#oilcontent) |  |
| polyphenols |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Polyphenols as a percentage of hop mass.<br /><br />Polyphenols are a large family of naturally occurring phenols with "several hydroxyl groups on aromatic rings".  They include four principal classes: phenolic acids, flavonoids, stilbenes, and lignans.  Polyphenols in hops contribute to the astringency and fullness of beer's taste, enhancing its overall flavor profile.  They do not have a direct aroma but can affect beer taste by contributing to its mouthfeel, astringency, and haze formation.  Additionally, they play a role in beer stability, as they have antioxidant properties that can help prevent the oxidation of flavor compounds. |
| xanthohumol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Xanthohumol as a percentage of hop mass.<br /><br />Xanthohumol is a natural flavonoid found in the female inflorescences of hops.  Its impact on beer taste is not as significant that of alpha acids or essential oils, but it may contribute to the overall complexity and subtle nuances in beer flavors.  (Xanthohumol has also been the subject of considerable research for its potential health benefits, but typically in quantities far exceeding any amount that could be obtained by ordinary dietary intake.) |
| inventory |  | [HopAmount](#hopamount) |  |


---

# Component Types

## HopAmount

The ways in which an amount of a Hop could be measured

## OilContent

Collects all information of a hop variety pertaining to oil content, polyphenols, and thiols. Each individual compound is expressed as a percent of the total oil measurement.

<strong>OilContent</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| total_oil_ml_per_100g |  | number | The total amount of oil, including hydrocarbons, esters, and terpene alcohols in units of ml of oil per 100g of hop mass. |
| myrcene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Myrcene as a percentage of total hop oil.<br /><br />Brad Smith writes "This is the most significant hop oil, making up from 30-60% of total hop oils in most varieties. Myrcene is often described as the “fresh hop oil” and has flavors and aroma varying from herbaceous to resinous, green, balsamic, and slightly metallic.  It is a major component in many hop varieties from the Pacific Northwest, and is therefore a critical oil in IPAs.  Cascade, for example has a myrcene content of nearly 60%.  Myrcene has a low boiling point and is highly volatile.  In fact it will virtually disappear in most boil additions, and even tends to be volatile in higher temperature whirlpool/steeping additions.  It also oxidizes very rapidly, and is probably best used in dry hop applications."  (See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/) |
| humulene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Humulene as a percentage of total hop oil.<br /><br />Brad Smith writes "The second largest hop oil by percentage, humulene makes up between 12% and 50% of total hop oils.  Humulene is responsible for earthy and spicy flavors found in traditional noble hops.  While humulene has a higher boiling point (around 106°C), it is very volatile and hydrophobic, so it is still best used in the whirlpool or dry hopping.  Humulene is also easily oxidized, though the oxidized humulene-epoxide III play a major role in the flavor of varieties like Hallertauer Mittelfrüh."  (See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/) |
| caryophyllene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Caryophyllene (more formally β-caryophyllene or BCP) as a percentage of total hop oil.<br /><br />Brad Smith writes "Caryophyllene makes up between 6% and 15% of total hop oils in most varieties.  It is a major compound in many aromatic plants including cloves, cannabis, rosemary, and hops.  It is also a significant aromatic compound in black pepper.  The aroma is described as woody, earthy, and peppery though it also has a strong herbal component.  The spicy, woody aroma is often evident when you crush dried hops in your hands.  Many English hop varieties such as East Kent Goldings have the largest percentage of caryphyllene giving them a woody, earthy finish.  While not quite as volatile as myrcene, caryophyllene it will boil quickly and is best used in the whirlpool or as a dry hop."  (See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/) |
| geraniol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Geraniol as a percentage of total hop oil.<br /><br />Brad Smith writes "Geraniol is an aromatic oil with a floral, sweet or rose aroma found in many American, New Zealand and Australian hops.  It is used in rose oil, palmarosa oil, and citronella oil, and is a component of common spices like lavender, nutmeg, coriander, rose and blackberry.  Many brewers also will add hops with geraniol during the tail end of active fermentation to promote tropical and citrus fruit flavors.  Hops with high geraniol have become popular for creating tropical/fruity IPA styles."  (See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/) |
| linalool |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Linalool as a percentage of total hop oil.<br /><br />Brad Smith writes "Related closely to Myrcene chemically, linalool has a floral aroma that smells like rose, orange, citrus or lavender.  It is more soluble in wort than myrcene, and also has a lower flavor threshold so it can be potent despite the small fraction it makes up of total hop oils.  Like geraniol, linalool is associated with many of the tropical, floral and citrus flavors that are popular in fruity and tropical IPAs."  (See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/) |
| farnesene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Farnesene as a percentage of total hop oil.<br /><br />Brad Smith writes "Farnesene is a volatile hop oil that is loosely associated with certain noble hops like Saaz, but can make up 10-20% of total hop oils in other noble hops like Tettnanger, Styrian hops and many American varieties.  It has a woody, herbal, citrus aroma and sometimes also takes on a floral character.  Because it is very volatile, it is rarely found in the finished beer unless it has been dry hopped.  [It] is often associated with varieties that take on a noble hop character, so if you see a hop high in Farnesene it likely has the aroma profile similar to many noble hops."  (See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/) |
| b_pinene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | β-Pinene as a percentage of total hop oil.<br /><br />Brad Smith writes "Though not a major hop oil, β-Pinene has a green-woody and piney aroma.  It is a monoterpene, commonly found in many plants and it is soluble in alcohol but not water."  (See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/) |
| a_pinene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | α-Pinene as a percentage of total hop oil.<br /><br />Alpha-Pinene (an isomer of beta-pinene) has a distinctly woody, herbal scent and can be found in cone-bearing trees and herbs like rosemary. |
| limonene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Limonene as a percentage of total hop oil.<br /><br />Limonene is a relatively stable monoterpene occurring naturally in citrus fruit peels, hops and numerous coniferous and broadleaved trees.  Limonene delivers a powerful citrus character, and is associated with punchy citrus based hops, such as Citra, Simcoe and Centennial. |
| nerol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Nerol as a percentage of total hop oil.<br /><br />Nerol is an isomer of geraniol.  Like geraniol, it has a sweet rose odor but it is considered to be fresher.  Its aroma is described as sweet, natural, neroli, citrus, magnolia, fresh, floral, green, lemon, and lime. |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.9.1) on 2026-10-16 at 22:16:29+0200.
