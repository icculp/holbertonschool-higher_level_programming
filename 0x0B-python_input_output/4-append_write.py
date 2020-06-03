#!/usr/bin/python3
"""
    Task 4 Module
"""


def append_write(filename="", text=""):
    """
        write to txt file using utf8
        create file if !exist
        append to existing content if file exists
        returns # of chars written
    """
    count = 0
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(str(text))
    return count
