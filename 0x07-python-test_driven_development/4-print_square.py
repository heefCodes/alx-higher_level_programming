#!/usr/bin/python3
"""
Module 4-print_square
Contain a size, which must be an integer or float

"""
    

def print_square(size):
    """
    print_sqaure method

    Args:
        size (_type_): length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
