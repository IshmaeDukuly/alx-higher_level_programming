#!/usr/bin/python3
import sys
#Ishmael Dukuly
def safe_print_integer_err(value):
    try:
        print("{:d}".forat(value))
        return (True)
    except (TypeError, ValueError):
        print("exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
