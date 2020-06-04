#!/usr/bin/python3
"""
    Task 14 module
"""


def pascal_triangle(n):
    """ prints a neat triangle """
    tri = []
    if n <= 0:
        return tri
    for i in range(1, n + 1):
        e = 1
        row = []
        for k in range(1, i + 1):
            row.append(e)
            e = int(e * (i - k) / k)
        tri.append(row)
    return tri
