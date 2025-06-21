There are no built-in string methods to reverse a string.
If you want to reverse a string you would have to implement it
in a way such as slicing or using list methods like so:

```python
s = "hello world"
reversed = s[::-1]
# or
reversed = "".join(reversed(list(s)))
```