#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Test for max_integer function'''

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-3, 5, 0]), 5)
        self.assertEqual(max_integer([1.2, 3.4, 5, 1.8, 10.5]), 10.5)
