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

    def test_rectangle_area(self):
        """ testing area up in this bitch """
        self.assertEqual(self.r1.area(), 1)
        self.assertEqual(self.r2.area(), 4)

    def test_rectangle_str(self):
        """ tests string up in this bitch """
        rrr = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rrr), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update(self):
        """ tests update function """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_update_more(self):
        """ tests update function """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (10) 1/3 - 4/2")

    def test_rectangle_to_dict(self):
        """ tests to_dict function """
        self.assertDictEqual(self.r2.to_dictionary(), {'id': 2, 'width': 2, 'height': 2, 'x': 2, 'y': 2})

    def tearDown(self):
        """ done testing, tear down """
        pass
