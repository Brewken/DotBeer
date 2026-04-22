# DotBeer — a file format for brewers
An open file format for storing and exchanging brewing data about recipes, ingredients, styles, equipment, brew days,
stock and so on.  DotBeer files have a <font color="green">**`.beer`**</font> extension, hence the name.



## Design Principles
* **Human Readable**

  At the cost of making the files slightly larger, this makes life easier for implementers and users.
  If a program has trouble reading a file, it can locate the problem for the user (eg "Do not recognise hop type at
  line X, column Y"), making it easier to determine whether the issue is with the code that wrote the file or that is
  trying to read it.

  Similarly, if a brewer has a lot of <font color="green">**`.beer`**</font> files and wants to search for ones
  referencing a particular type of hop, this is easy to do with any text search tool.

* **Automatic Validation**

  Being able to automatically validate a file against the schema has two large benefits.  Firstly, it makes it easier to
  debug code that generates <font color="green">**`.beer`**</font> files, and developers can be a lot more confident
  that their implementation is correct, than, say, with BeerXML where there is no published machine-readable schema.
  Secondly, it simplifies reading in files if you first validate them against the schema (because, after this is done,
  code can safely assume that all "required" fields are present in the file and that field types are valid etc).

* **Comments Allowed**

  It is useful in sample files to be able to include comments without invalidating the file.  But it is also useful for
  implementing software to be able to output comments in a file -- eg to note that an optional part of the file format
  has not yet been implemented.

* **Reference Implementation**

  Some of the problems with older formats, such as BeerXML and BeerJSON stem from the fact that they were finalised
  without any software having implemented them.  This meant that some errors or ambiguities in the standards did not
  come to light until later.  It also made it harder for early adopters to implement the format because there was no
  tool to generate sample files.

  Because Dot**Beer is the native file format of the open source [Brewtarget](https://www.brewtarget.beer), it is
  field-tested.  Developers of other brewing software can use Brewtarget to generate sample files, and can examine its
  source code to see how things things are implemented.

* **Schema Evolution**

  We should make it as easy as possible for the file format to evolve over time.  Eg, if a new field is added, it should
  not break existing software.  It should also be obvious from the documentation which fields are supported (or
  deprecated) in which version of the schema.

  As an implementer, you should not need to juggle multiple schemas to cope with older and newer versions of files.  The
  current version of the schema should tell you which fields are valid in which versions of the file.

* **Clear File Extensions**

  Users shouldn't need to care about the inner workings of the file format.  They should be able to tell from the file
  extension what the file is for.  For DotBeer:
  * the <font color="green">**`.beer`**</font> file extension means the file holds brewing data that can be read by a
    program such as [Brewtarget](https://www.brewtarget.beer)
  * the <font color="BlueViolet">**`.beer.schema`**</font> file extension means the file holds schema information that
    is used to define the structure (and validate the contents) of <font color="green">**`.beer`**</font> files.

## Technical
The underlying format is [JSONC](https://jsonc.org/).

DotBeer files have the <font color="green">**`.beer`**</font> file extension.

DotBeer schema files have the <font color="BlueViolet">**`.beer.schema`**</font> file extension.

## Licensing
DotBeer is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).  This means it can be used in both free and
commercial software.  (Only modifications to the DotBeer files themselves need to remain MPL licensed.)
