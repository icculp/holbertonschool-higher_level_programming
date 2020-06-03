#!/usr/bin/python3
"""
    Task 10 module
"""


def class_to_json(obj):
    """
        returns the dictionary description with simple data structure
    """
    return obj.__dict__
