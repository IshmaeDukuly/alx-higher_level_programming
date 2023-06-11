#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_value = []
    for y in range(len(my_list)):
        if my_list[y] % 2 == 0:
            my_value.append(True)
        else:
            my_value.append(False)
        return ( my_value)
