#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(str[n]) >= 97 and ord(str[n]) <=122:
            n = chr(ord(n) - 32)
        print("{}".format(n), end="")
    print("")
