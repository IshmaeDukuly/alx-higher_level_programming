#!/usr/bin/python3
"""This is  module a class MyInt that has inherits from int"""


    class MyInt(int):
        """
         Methods:
        __init__(self, number)
        __eq__(self, others)
        __ne__(self, others)
     """

    def __init__(self, number):
        """now initialize number"""
        self.number
    
        def __eq__(self, others):
            """

            return: True if the both are not equal
            """

            return self.number != others

        def __ne__(self, others):
            """
            Return:
            True if both not equal
            """
            return self.number == others
