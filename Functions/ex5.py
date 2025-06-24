def multiple_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1
    
multiple_of_three

# should print nothing, without parentheses the function isn't called