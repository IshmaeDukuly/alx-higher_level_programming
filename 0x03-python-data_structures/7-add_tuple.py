#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    y = tuple_a[:2] + (0, 0)
    x = tuple_b[:2] + (0, 0)
    return (y[0] + x[0], y[1] + x[1])

