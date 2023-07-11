#!/usr/bin/python3

"""

Consists of parent class BaseGeometry
with the instance method area and integer_validation

Entails subclass Rectangle
wtih private attributes with and heiht, validated by parent,
reach parent's area method and prints width __str__
"""


    BaseGeometry = __import__('7-base_geometry').BaseGeometry



    class Reactangle(BaseGeometry):
        """this inherits from BaseGeometry

        Methods:
            __init__(self, width, height)
            area(self)
            __str__

        """
        def __init__(self, width, height):
            """validate and then initialize width and height

            Args:
                width (int): private
                height (int): private
            """
            self.integer_validator("width", width)
            self.integer_validator("height", height)
            self.__width = width
            self.__height = height

            def area(self):
                """reach parent's empty method and returns area"""
                return self.__width * self.__height

            def __str__(self):
                """prints [Rectangle] <width>/<height>"""
                return "[{:s}] {:d}/{:d}".format(self.__class__.__name__.self__width, self.__height)
