# dotBeer 1.0.0

A dotBeer (<span style="color:green; font-weight: bold; font-family: monospace;">.beer</span>) file is a JSONC (JSON with comments allowed) document with a `DotBeer` root element.  A <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file should be validated against the dotBeer schema before being read.  The schema is split into the following sections (with a corresponding <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> file for each one):

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

When reading or writing a <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file, you need read or write `Recipe` record(s) after all the ingredients, processes and so on that the recipes refer to.  This is because each `Recipe` record cross-refers to ingredient additions, mash profile, style, etc in the same file. This avoids the duplication required in BeerXML and BeerJSON files.  Similarly, you will want to read or write any `StockPurchase` records (eg `StockPurchaseCulture`, `StockPurchaseHop`) after any `Recipe` record(s), as this will make processing cross-references easier.  NOTE that this only refers to order of processing.  The order of records inside the file is, for the most part, not important.  (The exceptions are boil steps, mash steps, fermentation steps and instructions, which need to appear in correct order.)

The version of the dotBeer schema is stored in the `$id` field in the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> files.  Eg <span style="color:Blue; font-weight: bold; font-family: monospace;">https://dotbeer.org/schema/1.0.0/DotBeer.beer.schema</span> is the `$id` field for version 1.0.0 of the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">DotBeer.beer.schema</span> file.  (The version should be the same in all the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> files!)

The schema uses semantic versioning (Major.Minor.Patch).  Versions prior to 1.0.0 are subject to breaking changes at any time.  From 1.0.0 onwards:

  - A **patch** change, eg 1.2.3 to 1.2.4, shouldn't break anything.  Eg we added or amended a description or, in certain circumstances, tweaked a constraint.  Software using the older schema (eg 1.2.3) can validate and read a file written with the newer schema (eg 1.2.4) and vice versa.
  - A **minor** change, eg 1.3.5 to 1.4.0, is backwards compatible.  Software using the newer schema (eg 1.4.0) can validate and read a file written with the older schema (eg 1.3.5), but the reverse is not true.
  - A **major** change, eg 1.5.7 to 2.0.0, is not backwards compatible.  It's likely that "new" software would need two versions of the schema and some additional logic to be able to read both new and old files.

You should always validate a <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file against the schema before reading it in, as your parsing code then does not need to check anything that schema validation has already ensured.

If a field is marked `deprecated` in the schema that usually means it should be supported for reading but not for writing.  This is how a field can be phased out without breaking backwards compatibility within a major version.

---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.0.0) on 2026-10-29 at 18:53:49+0100.