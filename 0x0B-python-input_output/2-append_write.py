#!/usr/bin/pyton3
"""
Consists function that appends to  text file and returns num chars added
"""


def append_write(filename="", text=""):
    """appends to text file and returns num chars added"""
    width open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
