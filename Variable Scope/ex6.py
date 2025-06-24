# the function print accesses 1
# the 1 initialized in my_function is a separate variable
# in a different scope

a = 1

def my_function():
    a = 2

my_function()
print(a)

