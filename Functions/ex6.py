def compare_by_length(string1, string2):
    length_of_1 = len(string1)
    length_of_2 = len(string2)

    if length_of_1 < length_of_2:
        return -1
    elif length_of_2 < length_of_1:
        return 1
    else:
        return 0

print(compare_by_length('patience', 'perseverance'))
print(compare_by_length('strength', 'dignity'))
print(compare_by_length('humor', 'grace'))