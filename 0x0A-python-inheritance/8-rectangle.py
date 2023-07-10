#!/usr/bin/python3
"""
consists parent BaseGeomtry
with the instance method area and the integer_validator

also consists subclass Rectangle
with private attributes of width and height, validated by parent
"""


    BaseGeometry =__import__("7-base_geomery").BaseGeometry



    class Rectangle(BaseGeometry):
        """inherits the BaseGeometry
        the Methods:
            __init__(self, width, height)
        """
        def __init__(self, width, height):
            """validate and then initialise width and height
            Args:
            width (int): private
            height (int): private
        """

        super().integer_validator('width', width)
        super().ineger_validator('height', height)
        self.__height = height
        self.__height = height

        def area(self):
            """extents parent's empty mthod and output the area"""
            return self.__width * self.__height

        def __str__(self):
            """prints [Rectangle] <width>/<height>"""
            return "[{:s}] {:d}/{:d}".format(self.__class__.___name__.
                    self>__width, self.__height)

