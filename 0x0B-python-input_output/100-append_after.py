#!/usr/bin/python3
"""
Module 100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword (search_string)
    1. recreate content in new_text by copying lines over
    2. append new_string after lines if needed
    3. overwrite file from beginning
    """
    with open(filename, mode="r+", encoding="utf-8") as myfile:
        new_txt = ""
        for line in myfile:
            new_txt += line
            if search_string in line:
                new_txt += new_string
        myfile.seek(0)
        myfile.write(new_txt)
