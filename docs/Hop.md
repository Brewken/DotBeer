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
| product_id |  | string | Producer’s product code or number for this item. |
| origin |  | string | Country of origin for the hop variety |
| year |  | string | Year of harvest.  (Note that this is intentionally not a number, as, for one thing, years are not generally formatted in the same way as numbers.) |
| form |  | Enum:<br>&nbsp;∙ `extract`<br>&nbsp;∙ `leaf`<br>&nbsp;∙ `leaf (wet)`<br>&nbsp;∙ `pellet`<br>&nbsp;∙ `powder`<br>&nbsp;∙ `plug` |  |
| alpha_acid_range |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) | The typical range of alpha acid for this type of hop. |
| beta_acid |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The actual beta acid content of the specific year's harvest (and batch) of this type of hop. |
| beta_acid_range |  | [Measurement::RangeOfPercentageSimple](./Measurement.md#rangeofpercentagesimple) | The typical range of beta acid for this type of hop. |
| hop_type |  | Enum:<br>&nbsp;∙ `aroma`<br>&nbsp;∙ `bittering`<br>&nbsp;∙ `flavor`<br>&nbsp;∙ `aroma/bittering`<br>&nbsp;∙ `bittering/flavor`<br>&nbsp;∙ `aroma/flavor`<br>&nbsp;∙ `aroma/bittering/flavor` |  |
| notes |  | string |  |
| six_month_alpha_loss |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | The percentage of hop alpha lost in 6 months of storage at room temperature (~20 °C).<br /><br />Note that this is percentage and not percentage points.  So, eg, if a hop starts out with 4.0% `alpha_acid` and has 25% `six_month_alpha_loss`, then we would expect its alpha acid to be 3.0% after six months in storage. |
| substitutes |  | string | Alternate hop varieties that can be used in place of this hop variety |
| cohumulone |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Cohumulone as a percentage of total hop alpha acids.<br /><br />Cohumulone is one of the three main alpha acids (with humulone and adhumulone), and typically makes up 20–50% of a hop's alpha acids.  It is somewhat more soluble than the others and isomerises a little more readily during the boil.  A long-standing view among brewers is that high-cohumulone hops give a harsher bitterness, although the evidence for this is mixed.  (See eg https://en.wikipedia.org/wiki/Humulone.) |
| oil_content |  | [OilContent](#oilcontent) |  |
| polyphenols |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Polyphenols as a percentage of hop mass.<br /><br />Polyphenols are a large family of naturally occurring phenols with "several hydroxyl groups on aromatic rings".  They include four principal classes: phenolic acids, flavonoids, stilbenes, and lignans.  Polyphenols in hops contribute to the astringency and fullness of beer's taste, enhancing its overall flavor profile.  They do not have a direct aroma but can affect beer taste by contributing to its mouthfeel, astringency, and haze formation.  Additionally, they play a role in beer stability, as they have antioxidant properties that can help prevent the oxidation of flavor compounds. |
| xanthohumol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Xanthohumol as a percentage of hop mass.<br /><br />Xanthohumol is a natural flavonoid found in the female inflorescences of hops.  Its impact on beer taste is not as significant as that of alpha acids or essential oils, but it may contribute to the overall complexity and subtle nuances in beer flavors.  (Xanthohumol has also been the subject of considerable research for its potential health benefits, but typically in quantities far exceeding any amount that could be obtained by ordinary dietary intake.) |


---

# Component Types

## HopAmount

The ways in which an amount of a Hop could be measured

## OilContent

Collects all information of a hop variety pertaining to oil content.  With the exception of `total_oil_ml_per_100g`, each individual compound is expressed as a percent of the total oil measurement.  See https://beersmith.com/blog/2024/12/19/major-aromatic-hop-oils-in-beer-brewing/ for details on several of the oils.

<strong>OilContent</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| total_oil_ml_per_100g |  | `0 <= x ` | The total amount of oil, including hydrocarbons, esters, and terpene alcohols in units of ml of oil per 100g of hop mass. |
| myrcene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Myrcene as a percentage of total hop oil.<br /><br />Usually the largest component of hop oil, often 30–60% in aroma varieties, and particularly high in many Pacific Northwest hops such as Cascade.  It gives fresh, green, resinous and herbaceous aromas.  Being very volatile and quick to oxidise, little of it survives the boil, and some is lost even in a hot whirlpool, so it mainly contributes via late and dry-hop additions. |
| humulene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Humulene as a percentage of total hop oil.<br /><br />Typically the second-largest component, at roughly 10–50% of total oil.  It gives woody, earthy and spicy aromas and is characteristic of traditional noble hops.  It is volatile and does not dissolve readily in wort, so is best used in the whirlpool or as a dry hop.  Its oxidation products (humulene epoxides) contribute to the aroma of aged noble hops such as Hallertauer Mittelfrüh. |
| caryophyllene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Caryophyllene (more formally β-caryophyllene) as a percentage of total hop oil.<br /><br />Typically 6–15% of total oil.  It gives woody, peppery, herbal and spicy aromas (it is also found in black pepper, cloves and rosemary), and is prominent in many English varieties such as East Kent Goldings.  It is less volatile than myrcene but still largely lost in the boil, so is best used late or as a dry hop. |
| geraniol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Geraniol as a percentage of total hop oil.<br /><br />A floral, rose-like compound found in many American, New Zealand and Australian varieties, and potent even in small amounts.  Yeast can convert some of it into citronellol during fermentation, adding citrus character, which is one reason geraniol-rich hops are popular for fruity, tropical IPAs, and why some brewers dry hop while fermentation is still active. |
| linalool |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Linalool as a percentage of total hop oil.<br /><br />Gives floral, citrus and lavender-like aromas.  Although usually a small fraction of the oil, it is more soluble in wort than myrcene and has a low aroma threshold, so it can have a disproportionate effect on the finished beer.  Like geraniol, it is associated with the fruity, floral character of modern IPAs. |
| farnesene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Farnesene as a percentage of total hop oil.<br /><br />Varies widely between varieties: absent or trace in many, but a substantial share (around 10–20%) in some noble-type hops such as Saaz and Tettnanger.  It gives woody, herbal and sometimes floral or citrus notes, so a high farnesene content is a hint of noble-hop character.  It is very volatile and rarely survives into the beer except from dry hopping. |
| b_pinene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | β-Pinene as a percentage of total hop oil.<br /><br />A minor component with piney, green and woody aromas.  Like other monoterpenes, it dissolves poorly in water but readily in alcohol. |
| a_pinene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | α-Pinene as a percentage of total hop oil.<br /><br />Alpha-Pinene (an isomer of beta-pinene) has a distinctly woody, herbal scent and can be found in cone-bearing trees and herbs like rosemary. |
| limonene |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Limonene as a percentage of total hop oil.<br /><br />Limonene is a relatively stable monoterpene occurring naturally in citrus fruit peels, hops and numerous coniferous and broadleaved trees.  Limonene delivers a powerful citrus character, and is associated with punchy citrus based hops, such as Citra, Simcoe and Centennial. |
| nerol |  | [Measurement::PercentageSimple](./Measurement.md#percentagesimple) | Nerol as a percentage of total hop oil.<br /><br />Nerol is an isomer of geraniol.  Like geraniol, it has a sweet rose odor but it is considered to be fresher.  Its aroma is described as sweet, natural, neroli, citrus, magnolia, fresh, floral, green, lemon, and lime. |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-21 at 21:58:05+0200.
