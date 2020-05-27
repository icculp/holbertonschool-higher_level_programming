#!/usr/bin/python3
"""Task 31"""


class LockedClass:
    """LockedClass"""

    __slots__ = ['first_name']

    def __init__(self, val=""):
        """init"""
        self.first_name = val
