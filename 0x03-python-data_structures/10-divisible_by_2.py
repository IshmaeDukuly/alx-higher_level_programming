#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        val = []
        for y in my_list:
            if y % 2 is 0:
                val.append(True)
            else:
                val.append(False)
            return (val)
