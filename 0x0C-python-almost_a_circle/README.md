models/base.py, models/__init__.py : empty file __init__.py
    lass Base:
        private class attribute __nb_objects = 0
        class constructor: def __init__(self, id=None)::
            if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
            otherwise, increment __nb_objects and assign the new value to the public instance attribute id

This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

models/rectangle.py : class Rectangle that inherits from Base:

    In the file models/rectangle.py
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y

    If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
    If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
    If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0
