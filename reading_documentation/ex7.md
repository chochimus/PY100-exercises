From the documentation on Sequence Types and common sequence 
operations:
> An IndexError is raised if i is outside the sequence range.

Given the list ```['fish', 'and', 'chips']```, index position 10
is outside of the sequence range(0,2) and will throw an IndexError

this can be shown by running the following line in REPL:

```python
['fish', 'and', 'chips'][10]
# IndexError: list index out of range
```