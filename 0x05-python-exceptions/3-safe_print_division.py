#!/usr/bin/python3
#Ishmael Dukuly
def safe_print_division(a, b):
    """Here, returns the division"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside Result: {}".format(div))
    return (div)
