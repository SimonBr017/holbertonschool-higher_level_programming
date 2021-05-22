#!/usr/bin/python3
"""unction that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """text must be a string, otherwise raise a TypeError
    exception with the message text must be a string
    There should be no space at the beginning or
    at the end of each printed line"""

    string = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for c in text:
        if i == 0:
            if c == ' ':
                continue
            else:
                i = 1
        if i == 1:
            string += c
        if c in ('.', '?', ':'):
            string += "\n\n"
            i = 0
    print(string)
