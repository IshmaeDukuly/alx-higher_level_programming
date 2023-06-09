#!/usr/bin/python3
if __name__ == "__name__":
    import sys

    count = len(sys.argv) -1)
    if coun == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(count))
        for y in range(count):
            print("{} {}".format(y + 1, sys.argv[y + 1])
