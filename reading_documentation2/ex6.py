# str.join expects a single iterable object as argument
# it returns a string that is a concatenation of all the string values
# in the iterable and throws an error if any are not strings.
# also, the str used to call is used as the separator between elements.

print(". ".join(["one", "two", "three"])) # prints one, two, three

# while 
# print(".".join("this", "won't", "work")) causes an error
# as the function takes exactly one element