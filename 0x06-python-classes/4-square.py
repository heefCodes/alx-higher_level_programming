#!/usr/bin/python3
"""
Module 4-square with private size and public area
Define class Square
"""


class Square:
    """
    class definition

    Args:
        size: size of a side of square
    """
    def __init__(self, size=0):
        """
        Initializes Square

        Attribut:
            size (int, optional): _description_. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        A getter
        Return: size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter

        Args:
            value (_type_): set size to value, if int and greater than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate area of square

        Returns:
            area
        """
        return self.__size * self.__size
