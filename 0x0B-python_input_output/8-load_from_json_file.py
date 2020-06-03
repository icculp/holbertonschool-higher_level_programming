#!/usr/bin/python3
"""
    Task 8 Module
"""
import json


def load_from_json_file(filename):
    """
        creates an Object from a JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        l = json.load(f)
    return l
