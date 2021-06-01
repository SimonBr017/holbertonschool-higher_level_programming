#!/usr/bin/python3
"""class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """methode that return area of a rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """methode that print a string from an obj"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
