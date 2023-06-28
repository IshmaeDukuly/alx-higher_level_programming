#!/usr/bin/python3
#Ishmael Dukuly
def safe_print_division(a, b):
    """Here, rertuns the division"""
    try:
        div = m/n
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Result: {}".format(div))
    return (div)
