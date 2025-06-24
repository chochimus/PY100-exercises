def is_empty_or_blank(word):
    return word.strip(' ') == ''

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True