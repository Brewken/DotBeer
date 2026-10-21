# dotBeer 0.10.0

A dotBeer (<span style="color:green; font-weight: bold; font-family: monospace;">.beer</span>) file is a JSONC (JSON with comments allowed) document with a `DotBeer` root element.  A <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file should be validated against the DotBeer schema before being read.  The schema is split into the following sections (with a corresponding <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> file for each one):

#### Root element

  - [DotBeer](../docs/DotBeer.md)

#### Ingredients

  - [Fermentable](../docs/Fermentable.md)
  - [Hop](../docs/Hop.md)
  - [Misc](../docs/Misc.md)
  - [Culture](../docs/Culture.md)

#### Processes

  - [Mash](../docs/Mash.md)
  - [Boil](../docs/Boil.md)
  - [Fermentation](../docs/Fermentation.md)
  - [StepCommon](../docs/StepCommon.md)

#### Other freestanding elements used in a recipe

  - [Style](../docs/Style.md)
  - [Equipment](../docs/Equipment.md)
  - [Water](../docs/Water.md)

#### Recipe is best read or written after all above (see note below)

  - [Recipe](../docs/Recipe.md)

#### Inventory

  - [StockPurchase](../docs/StockPurchase.md)

#### Other

  - [Measurement](../docs/Measurement.md)

When reading or writing a <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file, you need read or write `Recipe` record(s) after all the ingredients, processes and so on that the recipes refer to.  This is because each `Recipe` record cross-refers to ingredient additions, mash profile, style, etc in the same file. This avoids the duplication required in BeerXML and BeerJSON files.  Similarly, you will want to read or write any `StockPurchase` records (eg `StockUseCulture`, `StockUseHop`) after any `Recipe` record(s), as this will make processing cross-references easier.  NOTE that this only refers to order of processing.  The order of records inside the file is, for the most part, not important.  (The exceptions are boil steps, mash steps, fermentation steps and instructions, which need to appear in correct order.)

The version of the DotBeer schema is stored in the `$id` field in the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> files.  Eg <span style="color:Blue; font-weight: bold; font-family: monospace;">https://dotbeer.org/schema/0.8.0/DotBeer.beer.schema</span> would be the `$id` field for version 0.8.0 of the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">DotBeer.beer.schema</span> file.  (The version should be the same in all the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> files!)

Schema versions prior to 1.0.0 are subject to breaking changes, but from 1.0.0 onwards adhere to the backwards compatibility principle.  This principle is that you should always be able to validate an older <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file against a newer schema (although the reverse is not guaranteed).  Eg, if a file were written using the 1.0.0 schema, it should validate and be readable against the 1.1.0 schema.

If a field is marked `deprecated` in the schema that usually means it should be supported for reading but not for writing.  This approach is part of what maintains the backwards compatibility principle.

---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-21 at 19:47:37+0200.