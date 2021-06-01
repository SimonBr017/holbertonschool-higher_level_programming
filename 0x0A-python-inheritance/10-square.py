#!/usr/bin/python3
"""class square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class square that inherit from rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
