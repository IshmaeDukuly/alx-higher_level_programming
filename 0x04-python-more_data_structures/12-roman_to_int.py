#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_sting) != str:
        return 0
    amount = 0
    figure = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'x': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        arabic = figure[roman]
        amount += arabic if amount < arabic *5 else -arabic
    return amount
