#!/usr/bin/python3
"""
Contains function that writes to text file and returns num and chars written
"""


def write_file(filename="", text=""):
    """Writes text to file and num chars written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
