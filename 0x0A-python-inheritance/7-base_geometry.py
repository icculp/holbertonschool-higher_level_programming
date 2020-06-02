#!/usr/bin/python3
"""
    Task 7 Module
"""


class BaseGeometry:
    """ empty class, thanks covid """

    def area(self):
        ''' misleading '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
