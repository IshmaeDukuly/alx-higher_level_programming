#!/usr/bin/python3
# Author by: Ishmael Dukuly
def divisible_by_2(my_list. idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
