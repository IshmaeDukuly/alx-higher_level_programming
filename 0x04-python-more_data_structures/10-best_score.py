#!/usr/bin/python3

def bes_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    highest = max(my_dict.val())
    for key, val in my_dict.items():
        if value is highest:
            return key
