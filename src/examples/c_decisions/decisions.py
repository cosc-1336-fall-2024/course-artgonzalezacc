def test_config():
    return True

def is_number_in_range(min_range, max_range, num):
    return num >= min_range and num <= max_range

def is_vowel(letter):#a e i o u
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

def is_consonant(letter):
    return not (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u')