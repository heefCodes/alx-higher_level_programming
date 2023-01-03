#!/usr/bin/python3
"""
Module 2-rectangle
"""


class Rectangle:
    """
    class Rectangle definition

    """

    def __init__(self, width=0, height=0):
        """
        Initializes class Rectangle

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method: to retrieve width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method: to set width value

        Args:
            value (int): set width to value, if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method: to retrieve height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method: set height

        Args:
            value (int): set height to value, if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        calculate the area of a rectangle

        Returns: area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate the perimeter of a rectangle

        Returns: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)
