#!/usr/bin/python3
"""
Module 11-square
Contains parent class Rectangle
with public instance method area and integer_validator
Contains subclass Square
with instantiation of private attributes size, validated by parent
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from BaseGeometry
    Methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """validate and initialize size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    # def area(self):
    #     """extends parent's empty method and returns area"""
    #     return self.__width * self.__height

    def __str__(self):
        """prints [Square] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
