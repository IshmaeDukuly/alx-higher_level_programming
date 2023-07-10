#!/usr/bin/python3
"""This is  module a class MyInt that has inherits from int"""


class MyInt(int):
     """
         Methods:
        __init__(self, num)
        __eq__(self, other)
        __ne__(self, other)
     """

    def __init__(self, num):
        """now initialize num"""
        self.num

     def __eq__(self, other):
            """
            return: True if the both are not equal
            """

            return self.num != other

     def __ne__(self, other):
            """
            Return:
            True if both not equal
            """
            return self.num == other
