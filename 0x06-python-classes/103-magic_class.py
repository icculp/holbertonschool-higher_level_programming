#!/usr/bin/python3
"""D"""
import math


class MagicClass:
    '''Defines a magicb'''
    def __init__(self, radius=0):
        '''fuck you'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        '''asdf'''
        return (self.__radius ** 2) * math.pi

    def circumference(self, radius):
        '''asdfjl'''
        return 2 * math.pi * self.__radius
