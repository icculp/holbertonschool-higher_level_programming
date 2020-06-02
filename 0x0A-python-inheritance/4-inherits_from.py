#!/usr/bin/python3
"""
    Task 4 Module
"""


def inherits_from(obj, a_class):
    """ True if obj type inherits directly from a_class, else False """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
