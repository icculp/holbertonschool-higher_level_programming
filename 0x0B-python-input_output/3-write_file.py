#!/usr/bin/python3
"""
    Task 3 Module
"""


def write_file(filename="", text=""):
    """
        write to txt file using utf8
        create file if !exist
        overwrite existing content if file exists
        returns # of chars written
    """
    count = 0
    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(str(text))
    return count
