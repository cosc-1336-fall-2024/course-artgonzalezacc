def test_config():
    return True

def is_number_in_range(min_range, max_range, num):
    return num >= min_range and num <= max_range

def is_vowel(letter):#a e i o u
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

def is_consonant(letter):
    return not (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u')

def is_number_even(num):
    return num % 2 == 0

def get_generation(year):

    generation = ""

    if year >= 1910 and year <= 1924:
        generation = "The Greatest Generation"
    elif year >= 1925 and year <= 1945:
        generation = "The Silent Generation"
    elif year >= 1946 and year <= 1964:
        generation = "Baby Boomer Generation"
    elif year >= 1965 and year <= 1979:
        generation = "Generation X"
    elif year >= 1980 and year <= 1994:
        generation = "Generation Y"
    elif year >= 1995 and year <= 2012:
        generation = "Generation Z"
    elif year >= 2013 and year <= 2024:
        generation = "Generation Alpha"
    else:
        generation = "Invalid Year"

    return generation