#!/usr/bin/python3
"""
This is the module a class MyInt that has inherits 
from int
"""


class MyInt(int):
   """The int operators == and !="""

def __eq__(self, value):
    """override == operator with != behavior """
    return self.real != value

def __ne__(self, value):
    """override the == operator with != behavior"""
    return self.real == value
