#!/usr/bin/python3
"""
consists parent class BaseGeometry
with public instance method and integr_validation

consists subclass square with private attribute size, validated by superclass
"""


Rectangle = __import__('9-rectangle').Rectangle



class square(Rectangle):
     """inherits from Rectangle, that inherits from BaseGeometry
     Method:
         __int__(self, size)

    """
     def __init__(self, size):
        """initiliazes size

        args:
        size (int): private

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
