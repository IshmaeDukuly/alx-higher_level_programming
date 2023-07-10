#!/usr/bin/python3
""""
The BaseGeometry
with public instance area
"""


class BaseGeomtry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """is not implemented"""
        raise Exception("area(self() is not implemented")


    def inter_validator(self, name, value):
        """ validates the input
        Arguments:
        name (str): always assumed a string
        value (ingeger): greater than zero
    """
    if type(value) is not int:
        raise TypeError("{:s} must be an integer".format(name))
    if value <= 0:
        raise valueError("{:s} must be greater than 0".format(name))
