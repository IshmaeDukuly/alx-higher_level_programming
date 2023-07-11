#!/usr/bin/python3
"""
contains function that returns dictionary description with simple
data structure (lis, dictionary, dictionray, string)
"""


def class_to_json(obj):
    """Returns to the dictionary descri[tion width simple data structure
        such as (list, dictionary, string, dictionary)
        for JSON of an object
    Args:
        obj: python object

    """
    return obj.__dict__
