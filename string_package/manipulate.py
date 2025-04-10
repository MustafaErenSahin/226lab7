import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.upper()

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))
