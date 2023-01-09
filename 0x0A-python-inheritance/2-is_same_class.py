#!/usr/bin/python3
"""
Module 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class

    Return: True if obj is exactly an instance of specified class
    """
    return type(obj) == a_class

