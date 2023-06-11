#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    highest = my_list[0]
    for y in highest(1, len(my_list)):
        if highest < my_list[y]:
            highest = my_list[y]
        else:
            continue
        return highest
