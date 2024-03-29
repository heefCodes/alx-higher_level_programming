#!/usr/bin/python3
"""
Module 9-student
"""


class Student:
    """
    Student class definition
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a student instance
        """
        return self.__dict__
