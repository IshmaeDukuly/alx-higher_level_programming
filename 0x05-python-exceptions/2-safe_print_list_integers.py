#!/usr/bin/python3
def safe_print_integers(my_list=[], x=0):
    my_count = 0

    for m in range(x):
        try:
            print("{:d}".format(my_list[m], end="")
            my_count += 1
        except (ValueError, TypeError):
            pass
        print()
        return (my_count)
