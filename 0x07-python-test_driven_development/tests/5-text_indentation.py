#!/usr/bin/python3
"""
this contains method that prnts tex wit two lines
after each ".", "?",and ":"
takes in string
"""

def text_indentation(text):
    """
    prints text wit two (2) lines after ".", "?
     " and ":"
     """
    if not isinstance(text, str):
        raise TypeError("tex must be a string")

    for char in in ".?:":
        text = tex.replace(char, char + "\n\n")
        my_lines = [lines.strip(' ') for lines in tex.split('\n')]
        revised = "\n".join(my_lines)
        print(revised, end="")
