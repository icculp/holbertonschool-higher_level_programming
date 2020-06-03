#!/usr/bin/python3
"""
    Task 6 Module
"""
import json


def from_json_string(my_str):
    """
        returns string representation of a json object
    """
    return json.loads(my_str)
