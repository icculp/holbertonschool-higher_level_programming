#!/usr/bin/python3
"""
    Task 0 Module
"""


def read_file(filename=""):
    """ reads txt file, prints to stdout """
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
