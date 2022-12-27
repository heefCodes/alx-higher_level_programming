#!/bin/python3
"""
Module 0-add_integer definition

"""
def add_integer(a, b=98):
    """
    add_integer method

    Args:
        a (int): first argument
        b (int, optional): second argument. Defaults to 98.

    Return: int(a) + int(b)

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)