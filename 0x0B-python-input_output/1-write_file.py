#!/usr/bin/python3
"""
Module 1-write_file that write a string to a text file
"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
