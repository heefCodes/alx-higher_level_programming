#!/usr/bin/python3
"""
Module 0-read_file
"""


def read_file(filename=""):
    """
    read_file function that read text file (UTF8)
    and print it to stdout

    Args:
        filename (str, optional): Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
