#!/usr/bin/python3
"""module who define a rectagle"""


class Rectangle:
    """class who defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """draw the recangle with '#'
        Returns string of # as a rectangle"""
        string_rect = ""
        if self.__height == 0 or self.__width == 0:
            return string_rect
        for i in range(self.__height):
            string_rect += ("#" * self.__width)
            if i < (self.height - 1):
                string_rect += "\n"
        return string_rect

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print a message when the rectangle is killed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width + self.__height) * 2
