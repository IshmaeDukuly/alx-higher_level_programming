#!/usr/bin/python3
# Author by Ishmael
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return 'none'
    else:
        return my_list[idx]
