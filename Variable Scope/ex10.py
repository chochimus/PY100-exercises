# b[0] will access the global variable b's first element here

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)