#!/usr/bin/python3
"""
contains method inherites_from
output True if the object is the insatnce class that inherites 
"""


def inherites_from(obj, a_class):
    """
    Return: True if object is instance of class that inherites from
    """

    return (type(obj) is not a_class and issubclass(type(obj), a_class))
