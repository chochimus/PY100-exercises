# I believe it prints 7, even though the variable is changed
# it is not updating the global variable only the local

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)