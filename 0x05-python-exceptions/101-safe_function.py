#!/usr/bin/python3
import sys
#Ishmael Dukuly
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as m:
        print("Exception: {}".format(m), file=sys.stderr)
        return None
