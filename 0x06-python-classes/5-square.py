#!/usr/bin/python3
"""
Module 5-square
Definition of class Square
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

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method

        Return: size
        """

        return self.size

    @size.setter
    def size(self, value):
        """
        Setter method

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
        Calculate area

        Returns:
            area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        print square with character #

        """
        square = ["#" * self.__size for rows in range(self.__size)]
        print("\n".join(square))
