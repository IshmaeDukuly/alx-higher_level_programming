#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        highest = my_list[0]
        for x in my_list:
            if x > highest:
                highest = x
            return (highest)
        else:
            return (None)




























