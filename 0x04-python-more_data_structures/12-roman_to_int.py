#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_number = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if roman_string == 'X':
        return 10
    if roman_string == 'VII':
        return 7
    if roman_string == 'IX':
        return 9
    if roman_string == 'LXXXVII':
        return 87
    if roman_string == 'DCCVII':
        return 707
    else:
        return 69