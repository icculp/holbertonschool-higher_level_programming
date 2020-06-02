#!/usr/bin/python3
"""
    Task 12 Module
"""


class MyInt(int):
    """ int with weird behavior """

    def __init__(self, value):
        ''' initialize '''
        self.__value = value
        super().__init__()

    def __eq__(self, other):
        ''' do opposite of == '''
        return self.__value != other

    def __ne__(self, other):
        ''' do opposite of == '''
        return self.__value == other
