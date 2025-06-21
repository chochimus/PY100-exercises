In the case of finding an index of a given element, you can use the
```str.index(x[, start[, end]])``` method, which returns the zero-based index in the list of the first item whos value equals x.
If no value is found a ValueError is thrown, so it is good practice to first check for existance.

for example given the list:

```python
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
```

you can determine the index using the method like so:
```python
fruist.index("cherry")
```