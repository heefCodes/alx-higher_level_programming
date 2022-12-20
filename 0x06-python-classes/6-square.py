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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes Square

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method

        Return: size
        """

        return self.__size

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

    @property
    def position(self):
        """
        Getter method

        Return: position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method

        Args:
            value (_type_): set size to value, if int and > 0

        """
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        square = [" " * self.position[0] + "#" * self.__size for rows in range(self.__size)]

        print("\n" * self.__position[1], end="")
        print("\n".join(square))
