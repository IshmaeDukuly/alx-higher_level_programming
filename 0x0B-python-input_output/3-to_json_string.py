#!/usr/bin/python3
"""
Contains function taht returns JSON representation of obj (string)
"""

def to_json_string(my_obj):
    """Return to JSON representation of obj (string)
    Args:
        my_obj: python obj
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)
