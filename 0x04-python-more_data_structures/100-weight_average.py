#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
            return (0)
        result = 0
        result_b = 0
        for m, n in my_list:
            result += m * n
            result_b += m
        return (result / result_b)
