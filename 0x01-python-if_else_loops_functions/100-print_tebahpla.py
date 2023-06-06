#!/usr/bin/python3
n1 = 0
for n in range(ord("z"), ord("a")-1, -1):
    print("{}".format(chr(n - n1)), end="")
    n1 = 32 if n1 == 0 else 0
