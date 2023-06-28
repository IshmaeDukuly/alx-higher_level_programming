#!/usr/bin/python3
#ishmael Dukuly
def magic_calculation(a, b):
    output = 0

    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            else:
                output += (a ** b) / m
        except Exception:
            output = b + a
            break
        return (output)
