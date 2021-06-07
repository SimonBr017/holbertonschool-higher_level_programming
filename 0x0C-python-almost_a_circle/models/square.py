#!/usr/bin/python3
"""class square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation"""
        return "[Square] (" + str(self.id) + ") " + str(
            self.x) + "/" + str(self.y) + " - " + str(
                self.width)

    """getter"""

    @property
    def size(self):
        return self.width

    """setter"""

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """public Method"""

    def update(self, *args, **kwargs):
        """Assign an argument to each attributes"""
        attributes = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}
