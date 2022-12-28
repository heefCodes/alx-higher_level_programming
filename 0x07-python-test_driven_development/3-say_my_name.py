#!/usr/bin/python3
"""
Module 3-say_my_name:
contain two arguments, first_name, last_name

"""
# def __init__(self, first_name, last_name):
#     """
#     Initializes say_my_name

#     Args:
#         first_name (_type_): _description_
#         last_name (_type_): _description_
#     """
#     self.first_name = first_name
#     self.last_name = last_name


def say_my_name(first_name, last_name=""):
    """
    say_my_name method definition

    Args:
        first_name (string)
        last_name (str, optional): Defaults to "".
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        return f'My name is {first_name} {last_name}'
