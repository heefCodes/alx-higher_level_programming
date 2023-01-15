#!/usr/bin/python3
"""
Module 5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function to save to json file

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return json.dump(my_obj, myfile)
