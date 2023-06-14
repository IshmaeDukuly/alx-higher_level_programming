#!/usr/bin/python3
def multiply_by_2(my_dict):
    dict_1 = my_dict.copy()
    for m in dict_1.keys():
        dict_1[m] *= 2
    return (dict_1)
