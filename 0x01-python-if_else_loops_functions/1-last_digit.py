#!/usr/bin/python3
import random 
number = random.randint(-10000, 10000)
figure = abs(number) % 10
if figure > 5:
    print("greater than 5")
    if number < 0:
        figure = -figure
    print("last digit of {} is {} and is ".format(number, digit), end="")
elif figure == 0:
    print("0")
else:
    print("less than 6 and not 0)

