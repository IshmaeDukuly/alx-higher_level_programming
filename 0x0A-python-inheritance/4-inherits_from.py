#!/usr/bin/python3
"""
contains the method inherits_from
output True if the object is the insatnce class that inherites 
"""


def inherits_from(obj, a_class):
    """
    Return: True if object is instance of class that inherits from
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
