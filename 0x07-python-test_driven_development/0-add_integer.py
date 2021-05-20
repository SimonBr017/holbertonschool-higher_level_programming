#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """
    add_integer
    a and b must be integer
    a and b must be first casted to integers if they are float
    returns int (a + b)
    if a or b not integer or floats:
        raise TypeError
    'a must be an integer' or 'b must be an integer'
    """

    if type(a) is float:
        a = int(a)
    elif type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is float:
        b = int(b)
    elif type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
