#!/usr/bin/python3
"""This is  module a class MyInt that has inherits from int
sneaky --> has == and != operators inverted
"""



class MyInt(int):
    """

    Methods:
        __init_(self, num)
        __eq__(self, other)
        __ne__(self, other)

        """

        def __init__(self, nm):
            """now initialize num"""
            self.num = num

            def __eq__(self, other):
                """

                Return: True if both are eqaul
                """

                return self.num != other

            def __ne__(self, other):
                """

                Return: True if both are eqaul

                """
                return self.num == other
