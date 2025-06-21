As per the documentation on Integer literals:

> Underscores are ignored for determining the numeric 
value of the literal. They can be used to group digits for
enhanced readability. One underscore can occur between digits,
and after base specifiers like 0x.

So, in order to write a large integer in a way that makes it easier
to read, we simply use underscores in-place of commas:
```321,414``` should be written ```321_414```