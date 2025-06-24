# before running I believe this function will print 1
# as the if statement results in True and a is in scope
# of the function

def my_function():
    a = 1

    if True:
        print(a)

my_function()

# running resulted in printing 1