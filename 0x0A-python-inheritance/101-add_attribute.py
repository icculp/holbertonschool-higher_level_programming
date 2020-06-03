#!/usr/bin/python3
"""
    Task 13 Module
"""


def add_attribute(obj, name, value):
    ''' adds attributes, if it can! '''
    '''
        return setattr(obj, name, value)
    '''
    d = dir(obj)
    if '__slots__' in d:
        if name in obj.__slots__:
            setattr(obj, name, value)
        else:
            raise TypeError("can't add new attribute")
    elif '__dict__' in d:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
