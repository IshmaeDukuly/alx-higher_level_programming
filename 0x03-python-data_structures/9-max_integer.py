#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        highest = my_list[0]
        for m in my_list:
            if m > highest:
                highest = m
            return (highest)
        else:
            return (none)
