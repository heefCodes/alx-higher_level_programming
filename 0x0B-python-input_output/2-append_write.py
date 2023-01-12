#!/usr/bin/python3
"""
Module 2-append_write
"""


def append_write(filename="", text=""):
    """
    function to append a string at the end of a text file

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return (myfile.write(text))
