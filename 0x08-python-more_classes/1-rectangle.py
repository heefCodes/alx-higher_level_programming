#!/usr/bin/python3
"""
Module 1-rectangle
Contain width: instance attribute
"""


class Rectangle:
    """
    class Rectangle definition

    """
    def __init__(self, width=0, height=0):
        """
        Initializes class Rectangle

        Args:
            width (int): width of the rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method: to retrieve the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method: to set the width value

        Args:
            value (int): set width to value, if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method: to retrieve the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method: to height to value

        Args:
            value (int): set height to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
