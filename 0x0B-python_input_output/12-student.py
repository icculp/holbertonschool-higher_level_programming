#!/usr/bin/python3
"""
    Task 12 module
"""


class Student:
    """
        a class that students don't attend
        GET IT?!?!
    """

    def __init__(self, first_name, last_name, age):
        ''' in it '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves dictionary representation of student '''
        if type(attrs) is list and all(isinstance(i, str) for i in attrs):
            newd = dict()
            for key in list(self.__dict__.keys()):
                if key in attrs:
                    newd[key] = self.__dict__[key]
            return newd
        else:
            return self.__dict__
