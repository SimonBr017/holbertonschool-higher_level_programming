#!/usr/bin/python3
"""class Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """def class recangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """methode that return a specific string"""
        return "[Rectangle] (" + str(self.id) + ") " + str(
            self.x) + "/" + str(self.y) + " - " + str(
                self.width) + "/" + str(self.height)

    """getter"""

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """Setter"""

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """public Method"""

    def area(self):
        """ returns the area value of the Rect"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Assign an argument to each attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y,
                "id": self.id, "height": self.height,
                "width": self.width}
