# before running I believe the following function will print 1
# a is not reassigned so the a in the function 

a = 1

def my_function():
    print(a)

my_function()

# a is global and the print in the function accesses the global a