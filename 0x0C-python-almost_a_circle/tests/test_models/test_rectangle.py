#!/usr/bin/python3
"""Unit test for module base"""

from logging import exception
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest
from os import path
import json


class RectangleTests (unittest.TestCase):
    """Test for class base"""
    
    def test_baseId(self):
        """tests for class base"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 7)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(5, 4)
        self.assertEqual(r4.id, 8)

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

    def test_area(self):
        self.assertEqual(Rectangle(5, 10).area(), 50)

    def test_display(self):
        with self.assertRaises(TypeError):
            r6 = Rectangle()
        try:
            r6 = Rectangle()
        except TypeError as exception:
            self.assertEqual(exception.args[0], "__init__() missing 2 required positional arguments: 'width' and 'height'")
        
        with self.assertRaises(TypeError):
            r6 = Rectangle()
        try:
            r6 = Rectangle(2)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "__init__() missing 1 required positional argument: 'height'")
        
        r6 = Rectangle(2, 3)
        self.assertEqual(r6.display(), print("##\n##\n##"))
        
        r6 = Rectangle(2, 3, 1)
        self.assertEqual(r6.display(),print(" ##\n ##\n ##"))
        
        r6 = Rectangle(2, 3, 2, 1)
        self.assertEqual(r6.display(), print("\n  ##\n  ##\n   ##"))

    def test_str_(self):
        r7 = Rectangle(2, 3, id=7)
        self.assertEqual(str(r7), "[Rectangle] (7) 0/0 - 2/3")

        r8 = Rectangle(2, 3, 1, 2, 8)
        self.assertEqual(str(r8), "[Rectangle] (8) 1/2 - 2/3")

    def test_update(self):
        r9 = Rectangle(2, 3, 1, 1, 10)
        r9.update(89)
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 6, 'x': 2, 'y': 2, 'width': 4, 'id': 89}"))

        r9.update(89, 1)
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 6, 'x': 2, 'y': 2, 'width': 1, 'id': 89}"))

        r9.update(89, 1, 2)
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 2, 'y': 2, 'width': 1, 'id': 89}"))

        r9.update(89, 1, 2, 3)
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 1, 'id': 89}"))

        r9.update(89, 1, 2, 3, 4)
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 4, 'width': 1, 'id': 89}"))
        
        r9.update(**{ 'id': 89 })
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 1, 'id': 89}"))

        r9.update(**{ 'id': 89, 'width': 1 })
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 1, 'id': 89}"))

        r9.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 1, 'id': 89}"))

        r9.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 2, 'width': 1, 'id': 89}"))

        r9.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(print(r9.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 4, 'width': 1, 'id': 89}"))

