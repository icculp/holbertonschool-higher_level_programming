#!/usr/bin/python3
""" Unittest module for testing models """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests for Base class """

    def setUp(self):
        """ setup for tests """
        self.rect = Rectangle(98, 98, id=98)
        self.r1 = Rectangle(1, 1, 1, 1, 1)
        self.r2 = Rectangle(2, 2, 2, 2, 2)

    def test_rectangle_docstring(self):
        """ tests for docstrings """
        self.assertIsNotNone(("models.rectangle").__doc__)
        self.assertIsNotNone(Rectangle.__doc__)

    def test_rectangle_class(self):
        """ test base class """
        self.assertIsInstance(self.rect, Rectangle)
        self.assertTrue(type(self.r1) is Rectangle)
        self.assertTrue(type(self.r2) is Rectangle)
        
    def test_aase_id(self):
        """ test base id """
        self.assertEqual(self.rect.id, 98)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)

    def test_rectangle_bad_values(self):
        """ testing bad init typechecking """
        with self.assertRaises(TypeError):
            Rectangle("1", "1")
        with self.assertRaises(TypeError):
            Rectangle(1, "1")
        with self.assertRaises(ValueError):
            Rectangle(0, 0)
        with self.assertRaises(TypeError):
            Rectangle(1.5, 1.5)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -3, 0)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1.5)
        

    def tearDown(self):
        """ done testing, tear down """
        pass
