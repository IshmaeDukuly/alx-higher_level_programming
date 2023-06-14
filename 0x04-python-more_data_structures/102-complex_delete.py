#!/usr/bin/python3
def complex_delete(my_dict, value):
    my_target = []
    for key, key_value in my_dict.items():
        if key_value is value:
            my_target.append(key)
    for y in my_target:
        del my_dict[y]
    return(my_dict)
