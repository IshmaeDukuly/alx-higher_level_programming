#!/usr/bin/python3
"""consists module defines a function that adds attributes to objects"""


def add-attribute(obj, att, value):
    """add the new attribute to the object if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
