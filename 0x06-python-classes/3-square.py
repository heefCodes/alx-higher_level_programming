#!/usr/bin/python3
"""
Module 3-square
Define class Square
"""


class Square:
    """
    class Square definition

    Arg:
        size: size of a square
    """
    def __init__(self, size=0):
        """
        Initializes Square

        Attribute:
            size: size of a square, default to 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
