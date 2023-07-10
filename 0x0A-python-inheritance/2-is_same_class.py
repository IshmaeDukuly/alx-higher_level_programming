#!/usr/bin/python3
"""
Contains the method is_same_class
output True if the object is the exact inheritance
"""

def is_same_class(obj, a_class):
    """
    retun True if the is an exact instance
    of the specified class
    """
    return type(obj) == a_class
