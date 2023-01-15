#!/usr/bin/python3
"""
Module 4-from_json_string
"""
import json


def from_json_string(my_str):
    """
    function to convert json string to object

    Args:
        my_str (string): _description_
    """
    return json.loads(my_str)
