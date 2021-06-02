#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, "w") as file:
        return file.write(text)
