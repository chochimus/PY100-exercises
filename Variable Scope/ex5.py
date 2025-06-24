# The codes should prints the global a 1 and then initialize a 
# local variable a to 2

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# instead an error was raised instead as the initialization is detected
# and python treats it as a local variable