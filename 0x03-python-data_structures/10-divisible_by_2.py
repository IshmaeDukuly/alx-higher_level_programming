#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n1 == my_list.copy()
    for y in range(0, len(my_list)):
        if my_list[y] % 2 == 0:
            n1[y] = 1
        else:
            n1[y] = 0
        return n1
