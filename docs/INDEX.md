# DotBeer 0.4.0

A DotBeer (<span style="color:green; font-weight: bold; font-family: monospace;">.beer</span>) file is a JSONC (JSON with comments allowed) document with a `DotBeer` root element.  A <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file should be validated against the DotBeer schema before being read.  The schema is split into the following sections (with a corresponding <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> file for each one):

#### Root element

  - [DotBeer](../docs/DotBeer.md)

#### Ingredients

  - [Fermentable](../docs/Fermentable.md)
  - [Hop](../docs/Hop.md)
  - [MiscIngredient](../docs/MiscIngredient.md)
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

#### Other

  - [Measurement](../docs/Measurement.md)

When reading or writing a <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file, we recommend you read or write `Recipe` record(s) after all the ingredients, processes and so on that the recipes refer to.  This is because, inside the `Recipe` record, there is enough information to eg identify each hop added to the recipe, but not all the information to recreate that hop record if it is not already present on the system reading the record.

The version of the DotBeer schema is stored in the `Version` field in the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">DotBeer.beer.schema</span> file.  Versions prior to 1.0.0 are subject to breaking changes, but from 1.0.0 onwards adhere to the backwards compatibility principle.  This principle is that you should always be able to validate an older <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file against a newer schema (although the reverse is not guaranteed).  Eg, if a file were written using the 1.0.0 schema, it should validate and be readable against the 1.1.0 schema.

If a field is marked `deprecated` in the schema that usually means it should be supported for reading but not for writing.  This approach is part of what maintains the backwards compatibility principle.

---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.4.0) on 2026-08-17 at 19:53:38+0200.