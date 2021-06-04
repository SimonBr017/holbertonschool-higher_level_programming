#!/usr/bin/python3
"""Unit test for module base"""

from logging import exception
from models.rectangle import Rectangle
import unittest


class RectangleTests (unittest.TestCase):
    """Test for class base"""
    
    def test_baseId(self):
        """tests for class base"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(5, 4)
        self.assertEqual(r4.id, 7)

    def test_rectangle_value(self):
        """tests for rectangle class value"""
        
         
        with self.assertRaises(TypeError):
            r5 = Rectangle("1", 2)
        try:
            r5 = Rectangle("1", 2)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2")
        try:
            r5 = Rectangle(1, "2")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "height must be an integer")

        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 2)
        try:
            r5 = Rectangle(0, 2)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")
            
        with self.assertRaises(ValueError):
            r5 = Rectangle(2, 0)
        try:
            r5 = Rectangle(2, 0)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "height must be > 0")

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, "3", 4)
        try:
            r5 = Rectangle(1, 2, "3", 4)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, "4")
        try:
            r5 = Rectangle(1, 2, 3, "4")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")

        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, -1, 3)
        try:
            r5 = Rectangle(1, 2, -1, 3)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0")
            
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, 3, -3)
        try:
            r5 = Rectangle(1, 2, 3, -3)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")
