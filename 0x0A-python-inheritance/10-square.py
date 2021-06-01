#!/usr/bin/python3
"""class Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class square that inherit from rectangle"""

    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
