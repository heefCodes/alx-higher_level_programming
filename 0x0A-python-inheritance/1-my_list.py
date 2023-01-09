#!/usr/bin/python3
"""
Module 1-my_list
Contain class MyList and public instance method
that print list in sorted order
"""


class MyList(list):
    """
    MyList class that inherit from list
    """
    def print_sorted(self):
        """
        Print the list in sorted order
        """
        print(sorted(self))
