#!/usr/bin/python3
"""
Module 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj (_type_): _description_
        a_class (_type_): _description_
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
