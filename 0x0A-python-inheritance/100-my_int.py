#!/usr/bin/python3
"""This is my a class MyInt that has inherits from int"""


class MyInt(int):
   """The int operators == and !="""


def __eq__(self, value):
    """overide == operator with != behavior"""
    return self.real != value

def __ne__(self, value):
    """override the == operator with != behavior"""
    return self.real == value
