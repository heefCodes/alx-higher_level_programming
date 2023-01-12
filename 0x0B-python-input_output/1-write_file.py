#!/usr/bin/python3
"""
Module 1-write_file that write a string to a text file
"""


def write_file(filename="", text=""):
    """
    function to write to a file

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        number of character writen
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return (myfile.write(text))
