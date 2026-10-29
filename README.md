# dotBeer — a file format for brewers
An open file format for storing and exchanging brewing data about recipes, ingredients, styles, equipment, brew days,
stock and so on.  DotBeer files have a <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> extension, hence the name.

DotBeer draws on the experience of prior open-source brewing formats (BeerXML and BeerJSON) and shares a number of concepts and structures with them.  It is simpler than BeerJSON and more complete than BeerXML.

Detailed documentation is [here](./docs/INDEX.md).


## Design Principles
* **Human Readable**

  At the cost of making the files slightly larger, this makes life easier for implementers and users.
  If a program has trouble reading a file, it can locate the problem for the user (eg "Do not recognise hop type at
  line X, column Y"), making it easier to determine whether the issue is with the code that wrote the file or that is
  trying to read it.

  Similarly, if a brewer has a lot of <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> files and wants to search for ones
  referencing a particular type of hop, this is easy to do with any text search tool.


* **Automatic Validation**

  Being able to automatically validate a file against the schema has two large benefits.  Firstly, it makes it easier to
  debug code that generates <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> files, and developers can be a lot more confident
  that their implementation is correct than, say, with BeerXML where there is no published machine-readable schema.
  Secondly, it simplifies reading in files if you first validate them against the schema (because, after this is done,
  code can safely assume that all "required" fields are present in the file and that field types are valid etc).  So
  you should always validate a file against the schema before reading it in: your parsing code then does not need to
  check anything that schema validation has already ensured.


* **Comments Allowed**

  It is useful in sample files to be able to include comments without invalidating the file.  But it is also useful for
  implementing software to be able to output comments in a file -- eg to note that an optional part of the file format
  has not yet been implemented.
 
  Similarly, in the schema files themselves, there are comments explaining why things have been done in a particular 
  way, which is useful for implementers to understand. 


* **Reference Implementation**

  Some of the problems with older formats, such as BeerXML and BeerJSON stem from the fact that they were seemingly finalised
  without any software having fully implemented them.  This meant that some errors or ambiguities in the standards did not
  come to light until later.  It also made it harder for early adopters to implement the format because there was no
  tool to generate sample files.

  Because dotBeer is the native file format of the open source [Brewtarget](https://www.brewtarget.beer), it is
  field-tested.  Developers of other brewing software can use Brewtarget to generate sample files, and can examine its
  source code to see how things are implemented.


* **Schema Evolution**

  We should make it as easy as possible for the file format to evolve over time, and it should be clear from the version
  number what a change means for existing software (see [Versioning](#versioning) below).  It should also be obvious
  from the documentation which fields are supported (or deprecated) in which version of the schema.

  Within a major version, as an implementer, you should not need to juggle multiple schemas to cope with older and newer
  versions of files: the latest version of the schema will validate files written with any earlier version that has the
  same major version number.


* **Clear File Extensions**

  Users shouldn't need to care about the inner workings of the file format.  They should be able to tell from the file
  extension what the file is for:
  * The <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file extension means the file holds brewing data that can be read by a
    program such as [Brewtarget](https://www.brewtarget.beer).  These are the files seen and used by end users.
  * The <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> file extension means the file holds schema information that
    is used to define the structure (and validate the contents) of <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> files.  These
    are needed primarily by implementers.


* **Open Licensing**

  DotBeer is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).  This means it can be used in both free and
  commercial software.  (Only modifications to the dotBeer files themselves need to remain MPL licensed.)

## Technical
DotBeer files have the <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> file extension.

DotBeer schema files have the <span style="color:BlueViolet; font-weight: bold; font-family: monospace;">.beer.schema</span> file extension.

The underlying format for both types of file is [JSONC](https://jsonc.org/) --- ie JSON with comments allowed.

### File format details
JSONC is not (yet) tightly standardised, and different JSON parsers accept different extensions, so, to be precise, a
dotBeer file is a JSON text as defined by [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) with the following
additions and restrictions:

* **Comments are allowed** wherever whitespace is allowed, in both C++ style (`// ...` to the end of the line) and C
  style (`/* ... */`, which do not nest).
* **No other extensions are allowed.**  In particular, there are no trailing commas, no single-quoted strings, no
  unquoted keys, and no `NaN`, `Infinity` or `-Infinity` (ie all numbers are finite).
* **Keys must be unique** within each object.  (RFC 8259 only says they SHOULD be unique, and parsers differ over what
  they do with duplicates: eg some keep the first value and others, including Boost.JSON, keep the last.  So a file with
  duplicate keys might be read differently by different programs.)
* **Encoding is UTF-8**, without a byte order mark.

These rules match what [Boost.JSON](https://www.boost.org/doc/libs/release/libs/json/) accepts when `allow_comments` is
set and its other `parse_options` are left at their defaults, except that Boost.JSON does not reject duplicate keys.  Note that JSON Schema validation cannot check any of these rules, as
the validator only sees the result of parsing the file.  (`scripts/validate.py` does check them.)

### Versioning
The schema uses [semantic versioning](https://semver.org/), ie a three-part Major.Minor.Patch version number.  The
version is in the `$id` of every schema file, and every dotBeer file records, in its `version` field, the version of the
schema it was written with.  From version 1.0.0 onwards:

* A **patch** change, eg 1.2.3 to 1.2.4, shouldn't break anything.  Eg we added or amended a description or, in certain
  circumstances, tweaked a constraint.  Software using the older schema (eg 1.2.3) can validate and read a file written
  with the newer schema (eg 1.2.4) and vice versa.
* A **minor** change, eg 1.3.5 to 1.4.0, is backwards compatible.  Software using the newer schema (eg 1.4.0) can
  validate and read a file written with the older schema (eg 1.3.5), but the reverse is not true.
* A **major** change, eg 1.5.7 to 2.0.0, is not backwards compatible.  It's likely that "new" software would need two
  versions of the schema and some additional logic to be able to read both new and old files.

Versions prior to 1.0.0 are subject to breaking changes at any time.

As noted above, you should always validate a file against the schema before reading it in.  Checking the file's
`version` first lets you give the user a more helpful message (eg "This file was written by a newer version of
Brewtarget") than a schema validation error would when a file is too new for your software to read.

### Getting the schema
The definitive copy of each version of the schema is the corresponding release on GitHub (see
[Releases](https://github.com/Brewken/DotBeer/releases)).  To be certain that you have a current, released version of
the schema, get it from there.

Between releases, the head of the repository is a *draft* of the next version, and may change before that version is
released -- even though the version number in its `$id`s is already that of the next version.  (Eg, until 1.0.0 is
released, the head of the repository is a draft of 1.0.0.)  The same is true for BeerJSON.

Note that, as is normal for JSON Schema, the `$id` URLs in the schema files (eg
`https://dotbeer.org/schema/1.0.0/DotBeer.beer.schema`) identify the schemas, but are not necessarily locations from
which they can be downloaded.  Software that validates dotBeer files should use local copies of the schema files (as
`scripts/validate.py` and Brewtarget do) rather than relying on fetching them over the internet.

Detailed documentation is generated in the `docs` directory from the schema files in the `schema` directory by `scripts/generateDocs.py`.  All documentation is available online at [www.dotbeer.org](https://www.dotbeer.org/).

The `scripts/generateDocs.py` has the following dependencies:
 - [`loguru`](https://loguru.readthedocs.io/en/stable/overview.html)
 - [`PyYAML`](https://pyyaml.org/)

Example <span style="color:green; font-weight: bold; font-family: monospace;">.beer</span> files are in the `examples`
directory.  `scripts/validate.py` checks them against the schema, and also checks the rules that JSON Schema cannot
express (eg that local IDs are unique and that references point to objects of the right type).  Files in
`examples/invalid` are deliberately broken, and each one states the errors it is expected to produce.  Similarly, files
in `examples/warnings` are valid, but contain values that `scripts/validate.py` warns are probably mistakes (eg an
equipment default batch size that won't fit in the kettle), and each one states the warnings it is expected to produce.
Run
`scripts/validate.py` with no arguments to check all the examples, or pass it your own files.  It depends on
[`jsonschema`](https://python-jsonschema.readthedocs.io/) (version 4.18 or later) plus the `rfc3339-validator` package (`pip install "jsonschema[format-nongpl]>=4.18"`).

## Contributing
If you have an issue or question related to dotBeer, please don't hesitate to [create an issue](https://github.com/Brewken/DotBeer/issues) or start or continue a [discussion](https://github.com/Brewken/DotBeer/discussions).