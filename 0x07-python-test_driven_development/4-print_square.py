#!/usr/bin/python3
"""
Entails method that print square number
Takes in an int size
"""


def print_square(size):
    """
    print the square with the numbe
    given int size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size > 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
