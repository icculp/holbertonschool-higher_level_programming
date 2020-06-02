#!/usr/bin/python3
"""
    Task 1 Module
"""


class MyList(list):
    """ Inhereits from list """

    def print_sorted(self):
        """ Sorts a list full of ints """
        srtd = self.copy()
        srtd.sort()
        print(srtd)
