#!/usr/bin/python3
"""
Module 4-inherits_from
"""


def inherits_from(obj, a_class):
    """

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
