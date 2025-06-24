speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
# 19 < 24 and (0 > 0 or 24 > 0) 
# True and (False or True)
# True and True
# True
print(is_moving)

# without parentheses 
# braking_force < acceleration and speed > 0 or acceleration > 0
# 19 < 24 and 0 > 0 or 24 > 0
# True and False or True
# False or True
# True
print(braking_force < acceleration and speed > 0 or acceleration > 0)
# While this still prints true, it is not logically equivalent to the
# other statement and parentheses are necessary