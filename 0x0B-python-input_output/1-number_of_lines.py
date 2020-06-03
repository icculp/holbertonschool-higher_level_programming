#!/usr/bin/python3
"""
    Task 1 Module
"""


def number_of_lines(filename=""):
    """ returns number of lines in txt file """
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
    return count
