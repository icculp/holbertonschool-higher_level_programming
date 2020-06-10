#!/usr/bin/python3
""" Unittest module for testing models """
import unittest
from models.base import Base
import pep8


class TestBase(unittest.TestCase):
    """ Tests for Base class """

    def setUp(self):
        """ setup for tests """
        self.base = Base()
        self.b1 = Base(1)
        self.b2 = Base(2)
        self.base2 = Base()
        self.base3 = Base("wrong")
        self.basen = Base(-10)

    def test_base_docstring(self):
        """ tests for docstrings """
        self.assertIsNotNone(("models.base").__doc__)
        self.assertIsNotNone(Base.__doc__)

    def test_base_class(self):
        """ test base class """
        self.assertIsInstance(self.base, Base)
        self.assertTrue(type(self.base2) is Base)
        self.assertTrue(type(self.b1) is Base)
        self.assertTrue(type(self.b2) is Base)
        
    def test_aase_id(self):
        """ test base id """
        self.assertEqual(self.base.id, 1)
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.basen.id, -10)
        self.assertEqual(self.base3.id, "wrong")

    def test_base_wrong_2(self):
        """ bad init """
        self.assertRaises(TypeError, Base(), "wrong")

    def test_to_json_string(self):
        """ tests static method """
        self.assertEqual(self.base.to_json_string([]), '[]')
        self.assertEqual(self.base.to_json_string([{'x': 2}, {'width': 10}]), '[{\"x\": 2}, {\"width\": 10}]')
#       self.assertRaises(ValueError, self.base.to_json_string(), [{'1': 2}])

    def test_pep8(self):
        """ tests pep8 up in this bitch """
        p = pep8.StyleGuide(quiet=True)
        r = p.check_files(['models/base.py'])
        self.assertEqual(r.total_errors, 0)

    def tearDown(self):
        """ done testing, tear down """
        pass
