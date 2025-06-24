sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# without running, admission price should be 3.99 as 
# sale is True, not True evaluates to False so the if statement
# isn't reached, and instead the else statement is executed