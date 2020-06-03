#!/usr/bin/python3
"""
    Task 2 Module
"""


def read_lines(filename="", nb_lines=0):
    """ returns number of lines in txt file """
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if count < nb_lines or nb_lines <= 0:
                print(line, end='')
                count += 1
            else:
                break
