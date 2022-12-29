#!/usr/bin/python3
"""
Module 5-text_indentation
Containing text, which must be a string
print a text with 2 new lines after each of these characters:
1: .
2: ?
3: :
"""


def text_indentation(text):
    """
    text_indentation method definition

    Args:
        text (string): _description_
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for char in ".?:":
            text = text.replace(char, char + "\n\n")
            list_lines = [lines.strip(' ') for lines in text.split('\n')]
            revised = "\n".join(list_lines)
            print(revised, end="")
