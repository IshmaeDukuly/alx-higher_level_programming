#!/usr/bin/python3
"""
This contains method that returns an int
sum and Accepts two values and also whether int or float"""


def add_integer(a, b=98):
    """
    Return a + b as int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
