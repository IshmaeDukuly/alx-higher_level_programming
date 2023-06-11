#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n1 in row:
            print("{:d}".format(n1), end=" " if n1 != row[-1] else "")
         print()
