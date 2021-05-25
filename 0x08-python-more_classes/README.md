0-rectangle.py : empty class Rectangle that defines a rectangle

1-rectangle.py : class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
            width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
            if width is less than 0, raise a ValueError exception with the message width must be >= 0
    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
            height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
            if height is less than 0, raise a ValueError exception with the message height must be >= 0
    Instantiation with optional width and height: def __init__(self, width=0, height=0):

    2-rectangle.py: (based on 1-rectangle.py)
    Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter:

    if width or height is equal to 0, perimeter is equal to 0

3-rectangle.py: