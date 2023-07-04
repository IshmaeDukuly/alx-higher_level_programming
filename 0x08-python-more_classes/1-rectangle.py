#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This represents for rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
    Args:
        width: represents the width of the rectangle
        height: this represents the height of the rectangle
    Raises:
    TypeError: if the size is not an integer
    ValueError: if the size is less than 0
    """

    self.width = width
    self.height = height


    @property
    def width(self):
        """retrieves this attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise (ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """retrieves the height atribute"""
            return self.__height


        @height.setter
        def height(self, value):
            """sets height attribute"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
             self.__height = value


