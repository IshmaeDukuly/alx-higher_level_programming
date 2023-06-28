#!/usr/bin/python3
#ishmael Dukuly
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (valueError, typeError)
        return False
