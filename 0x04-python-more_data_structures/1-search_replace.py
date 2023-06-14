#!/usr/bin/python3
# Auhtor by: Ishmael Dukuly
def search_replace(my_list, search, replace):
    return (list(map(lambda y: replace if y is search else y, my_list))
