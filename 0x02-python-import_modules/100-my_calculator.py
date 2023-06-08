#!/usr/bin/python3
# Author by: Ishmael Dukuly
from calculator-1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) !:4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
        op = argv[2]
        if = {"+": add, "-": sub "*": mul, "/": div}
        if op not in f:
            print("Unkown operator. Available operators: +, -, * and /")
            exit(1)

            a = int(argv[1])
            b = int(argv[3])
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, f[op](a, b)))
