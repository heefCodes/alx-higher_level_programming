#!/usr/bin/python3
"""
Module 100-my_int
Contain base class int
Contain subclass MyInt
"""


class MyInt(int):
    """
    Contain:
    __init__(self, number)
    __eq__(self, value)
    __ne__(self, value)
    """

    def __init__(self, number):
        """initialize num"""
        self.number = number

    def __eq__(self, value):
        """
        Return:
           True if both not equal
        """
        return self.number != value

    def __ne__(self, value):
        """
        Return:
           True if both equal
        """
        return self.number == value
