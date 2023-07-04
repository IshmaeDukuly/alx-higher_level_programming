#!/usr/bin/python3
#ishmael
"""
this entails method that will print out
full name. Takes in strings: first and
last name
"""

def say_my_name(first_name, last_name=""):
    """
    prints 'My name is [full name]"
    """

    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} [:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string".format("firt_name" if isinstance(last_name, str)
            else ("last_name"))
