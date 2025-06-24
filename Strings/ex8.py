import string

def capitalize_words(sentence):
    return string.capwords(sentence)

my_string = 'launch school tech & talk'
print(capitalize_words(my_string))