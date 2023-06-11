#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n1 in row:
            if n1 is not row[len(row) -1]:
                print("{:d}".format(n1), end="")
            else:
                print("{:d}".format(n1), end="")
            print()
