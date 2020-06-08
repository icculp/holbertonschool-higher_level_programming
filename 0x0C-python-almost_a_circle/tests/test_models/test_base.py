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
        self.b2 = Base(2)
        self.base2 = Base()

    def test_base_class(self):
        """ test base class """
        self.assertTrue(type(self.base) is Base)
        self.assertTrue(type(self.base2) is Base)
        self.assertTrue(type(self.b1) is Base)
        self.assertTrue(type(self.b2) is Base)
        
    def test_aase_id(self):
        """ test base id """
        self.assertEqual(self.base.id, 1)
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.base2.id, 2)


    def tearDown(self):
        """ done testing, tear down """
        pass
