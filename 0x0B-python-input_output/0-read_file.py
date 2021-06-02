#!/usr/bin/python3
"""function to read a file"""


def read_file(filename=""):
    """read a file"""
    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
