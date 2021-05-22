#!/usr/bin/python3
"""unction that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    string = ""
    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in text:
        string += c
        if c in ('.', '?', ':'):
            string += "\n\n"
    print(string)
