# a printed in this case is 2 as the global var is changed

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# 2 was indeed printed