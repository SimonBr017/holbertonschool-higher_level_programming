#!/usr/bin/python3
"""unction that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """text must be a string, otherwise raise a TypeError
    exception with the message text must be a string
    There should be no space at the beginning or
    at the end of each printed line"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    leap = True
    for c in text:
        if not (c is ' ' and leap is True):
            print(c, end="")
            leap = False
            if c in [':', '.', '?']:
                print()
                print()
                leap = True
