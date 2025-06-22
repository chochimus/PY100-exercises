# while str.find() can be used to find the position of a substr,
# if one just needs to check if a string contains a substr the
# in operator can be used instead.
# As per the documentation: For the string and bytes types, x in y is True
# if and only if x is a substring of y

print("in" in "string") # True
print("not" in "string") # False