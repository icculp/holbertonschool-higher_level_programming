#!/usr/bin/python3
"""
    Task 7 Module
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Writes object to text file using json representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
