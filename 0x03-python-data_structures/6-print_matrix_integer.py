#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n_row in matrix:
        for n1 in n_row:
            if n1 is not n_row[len(row) -1]:
                print("{:d}".format(n1), end=" ")
            else:
                print("{:d}".format(n1), end="")
            print()
