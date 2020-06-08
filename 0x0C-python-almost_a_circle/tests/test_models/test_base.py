#!/usr/bin/python3
""" Unittest module for testing models """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Tests for Base class """

    def setUp(self):
        """ setup for tests """
        self.base = Base()
        self.b1 = Base(1)



    def tearDown(self):
        """ done testing, tear down """
        ?
