#!/usr/bin/python3
""" Unittest module for testing models """
import unittest
from models.square import Square
import pep8


class TestSquare(unittest.TestCase):
    """ Tests for Base class """

    def setUp(self):
        """ setup for tests """
        self.sq = Square(9, id=9)
        self.s1 = Square(1, 1, 1, 1)
        self.s2 = Square(2, 2, 2, 2)

    def test_sqr_docstring(self):
        """ tests for docstrings """
        self.assertIsNotNone(("models.square").__doc__)
        self.assertIsNotNone(Square.__doc__)

    def test_sqr_class(self):
        """ test base class """
        self.assertIsInstance(self.sq, Square)
        self.assertTrue(type(self.s1) is Square)
        self.assertTrue(type(self.s2) is Square)
        
    def test_asqr_id(self):
        """ test base id """
        self.assertEqual(self.sq.id, 9)
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)

    def test_square_bad_values(self):
        """ testing bad init typechecking """
        with self.assertRaises(TypeError):
            Square("1", "1")
        with self.assertRaises(TypeError):
            Square(1, "1")
        with self.assertRaises(ValueError):
            Square(0, 0)
        with self.assertRaises(TypeError):
            Square(1.5, 1.5)
        with self.assertRaises(ValueError):
            Square(1, 1, -3, 0)
        with self.assertRaises(TypeError):
            Square(1, 1, 1.5)

    def test_square_area(self):
        """ testing area up in this bitch """
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.sq.area(), 81)

    def test_square_str(self):
        """ tests string up in this bitch """
        rrr = Square(4, 2, 1, 12)
        self.assertEqual(str(rrr), "[Square] (12) 2/1 - 4")

    def test_square_update(self):
        """ tests update function """
        r1 = Square(10, 10, 10, 10)
        r1.update(89, 2, 4, 5)
        self.assertEqual(str(r1), "[Square] (89) 4/5 - 2")

    def test_square_update_more(self):
        """ tests update function """
        r1 = Square(10, 10, 10, 10)
        r1.update(x=1, id=2, y=3, size=4)
        self.assertEqual(str(r1), "[Square] (2) 1/3 - 4")

    def test_square_to_dict(self):
        """ tests to_dict function """
        self.assertDictEqual(self.s2.to_dictionary(), {'id': 2, 'size': 2, 'x': 2, 'y': 2})

    def test_pep8(self):
        """ tests pep8 up in this bitch """
        p = pep8.StyleGuide(quiet=True)
        r = p.check_files(['models/square.py'])
        self.assertEqual(r.total_errors, 0)

    def tearDown(self):
        """ done testing, tear down """
        pass
