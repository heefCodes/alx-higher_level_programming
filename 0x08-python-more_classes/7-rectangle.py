#!/usr/bin/python3
"""
Module 2-rectangle
"""


class Rectangle:
    """
    class Rectangle definition

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes class Rectangle

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """
        Print string character with "#"
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return rect

    def __repr__(self):
        """
        String representation of an object to create
        new object by using eval()
        """
        print(eval("Rectangle({:d}, {:d})".format(self.width, self.height)))

    def __del__(self):
        """
        Delete instance of class Rectangle
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
