#!/usr/bin/python3
"""
Module 11-student
"""


class Student:
    """
    Student class definition
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes Student class

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        Return:
            Transfer all attributes of json to self
        """
        for k, v in json.items():
            setattr(self, k, v)
