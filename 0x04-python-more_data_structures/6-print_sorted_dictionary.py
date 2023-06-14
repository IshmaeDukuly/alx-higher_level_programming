#!/usr/bin/pyton3
# Authored by: Ishmael Dukuly

def print_sorted_dictionary(a_dictionary):
    for m in sorted(a_dictionary.keys()):
        print("{}: {}".format(m, a_dictionary[m]))
