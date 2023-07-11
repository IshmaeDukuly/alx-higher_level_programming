#!/usr/bin/python3
"""
Consists of function taht returns int lists of pascal triangle of
any given size
"""


def pascal_triangle():
    """
    Return:
        An empty list [] if n <= 0
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for angle in range(n-1):
        trangle.append([a+b for a, b in zip([0]] + triangle[-1], triangle[-1] + [0])])
