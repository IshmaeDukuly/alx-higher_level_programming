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
        self.__width = width
        super().ineger_validator('height', height)
        self.__height = height

