#!/usr/bin/python3
"""
Module 6-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    function to create a python obj fro json file

    Args:
        filename (_type_): _description_
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        return json.load(myfile)
