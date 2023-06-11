#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    higher = my_list[0]
    for m in range(1, len(my_list)):
        if higher < my_list[m]:
            higher = my_list[m]
        else:
            continue
        return higher




























