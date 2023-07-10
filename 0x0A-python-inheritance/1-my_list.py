#!/usr/bin/python3

""""
This contains the class that inherite from the list
"""

class MyList(list):
    """ Inherits

    the methods:
    print_sorted(self)
    """

    def print_sorted(self):
        """Prints list of ints in sorted orderly"""
        print(sorted(self))
