#!/usr/bin/python3
"""Unit test for module square"""

from logging import exception
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest
import os
import json


class SquareTests (unittest.TestCase):
    """Test for class square"""
    
    def test_baseId(self):
        """tests for class square"""
        s1 = Square(1)
        self.assertEqual(s1.id, 37)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(1, 2)
        self.assertEqual(s2.id, 38)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.id, 39)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)

        with self.assertRaises(ValueError)as error:
            s5 = Square(-1)
        self.assertEqual("width must be > 0", str(error.exception))

        with self.assertRaises(ValueError)as error:
            s5 = Square(1, -2)
        self.assertEqual("x must be >= 0", str(error.exception))
        
        with self.assertRaises(ValueError)as error:
            s5 = Square(1, 2, -3)
        self.assertEqual("y must be >= 0", str(error.exception))

        with self.assertRaises(ValueError)as error:
            s5 = Square(0)
        self.assertEqual("width must be > 0", str(error.exception))

    def test_str_square(self):
        s7 = Square(2, id=7)
        self.assertEqual(str(s7), "[Square] (7) 0/0 - 2")

        s8 = Square(2, 1, 2, 8)
        self.assertEqual(str(s8), "[Square] (8) 1/2 - 2")
        
    def test_update(self):
        s9 = Square(2, 2, 2, 10)
        s9.update(89)
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size': 2, 'x': 2, 'y': 2, 'id': 89}"))

        s9.update(89, 1)
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size': 2': 2, 'id': 89}"))

        s9.update(89, 1, 2)
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size: 2, 'x': 2, 'y': 2, 'id': 89}"))

        s9.update(89, 1, 2, 3)
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size': 2, 'x': 3, 'y': 2, 'id': 89}"))

        
        s9.update(**{ 'id': 89 })
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size': 2, 'x': 3, 'y': 2, 'id': 89}"))

        s9.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size': 1, 'x': 3, 'y': 2, 'id': 89}"))

        s9.update(**{ 'id': 89, 'size': 1, 'x': 3 })
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size': 1, 'x': 3, 'y': 2, id': 89}"))

        s9.update(**{ 'id': 89, 'size': 2, 'x': 3, 'y': 4 })
        self.assertEqual(print(s9.to_dictionary()),
            print("{'size': 2, 'x': 3, 'y': 4, 'id': 89}"))
        
    def test_square_create(self):
        r11 = Square.create(**{ 'id': 89 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'size': 1, 'x': 0, 'y': 0, 'id': 89}"))

        r11 = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'size': 1, 'x': 0, 'y': 0, 'id': 89}"))

        r11 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'size': 1, 'x': 2, 'y': 0, 'id': 89}"))

        r11= Square.create(**{ 'id': 89,  'x': 2, 'y': 4 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'size': 1, 'x': 2, 'y': 4, 'id': 89}"))

    def test_square_string(self):
        with self.assertRaises(TypeError):
            s12 = Square("1")
        try:
            s12 = Square("1")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")
            
        with self.assertRaises(TypeError):
            s12 = Square(1, "2")
        try:
            s12 = Square(1, "2")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")
            
        with self.assertRaises(TypeError):
            s12 = Square(1, 2, "3")
        try:
            s12 = Square(1, 2, "3")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")
