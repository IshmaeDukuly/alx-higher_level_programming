#!/usr/bin/python3
def fizzbuzz():
    for fizz in range(1, 101):
        if fizz % 15 == 0:
            print("FizzBuzz ", end="")
        elif fizz % 3 == 0:
            print("Fizz ", end="")
        elif fizz % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(fizz), end="")
