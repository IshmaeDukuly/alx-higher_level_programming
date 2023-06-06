#!/usr/bin/python3
for n in range(0, 89):
    for n1 in range((n+1), 10):
        if (n != 8) or (n1 != 9):
            print("{}{}, ".format(n, n1), end="")
        else:
            print("{}{}".format(n, n1))
