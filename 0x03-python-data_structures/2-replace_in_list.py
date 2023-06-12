#!/usr/bin/python3
# Athor by: Ishmael Dukuly
def replace_int_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return(my_list)
