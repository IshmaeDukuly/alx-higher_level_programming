#!/usr/bin/python3
# Author by: Ishmael Dukuly
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list) - 1:
        return null
    else:
        return my_list[idx]
