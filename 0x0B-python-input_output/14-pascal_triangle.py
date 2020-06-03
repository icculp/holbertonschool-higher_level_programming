#!/usr/bin/python3
"""
    Task 14 module
"""

def pascal_triangle(n):
    """ prints a neat triangle """
    if n <= 0:
        return list()
    tri = []
    for i in range(n):
        for k in range(i):
            tri += [i + k]
    return tri
