#!/usr/bin/python3
"""Unit test for module rectangle"""

from logging import exception
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest
import os
import json
from io import StringIO
from contextlib import redirect_stdout


class RectangleTests (unittest.TestCase):
    """Test for class rectangle"""
    
    def test_baseId(self):
        """tests for class rectangle"""
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
        
        r6 = Rectangle(2, 2)
        stout = StringIO()
        with redirect_stdout(stout):
            r6.display()
        out = stout.getvalue()
        self.assertEqual(out, ("#" * 2 + "\n") * 2)
        
        r6 = Rectangle(2, 2, 1, 2)
        stout = StringIO()
        with redirect_stdout(stout):
            r6.display()
        out = stout.getvalue()
        self.assertEqual(out, "\n" * 2 + (" " * 1 + "#" * 2 + "\n") * 2)
        
        with self.assertRaises(TypeError):
            r6 = Rectangle()
        try:
            r6 = Rectangle().display()
        except TypeError as exception:
            self.assertEqual(exception.args[0], "__init__() missing 2 required positional arguments: 'width' and 'height'")
                
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

    def test_to_dictionary(self):
        r10 = Rectangle(1, 2, 3, 4)
        dic = {'x': 3, 'y': 4, 'id': 36, 'height': 2, 'width': 1}
        with self.subTest():
            self.assertEqual(r10.to_dictionary(), dic)

    def test_rectangle_create(self):
        r11 = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'height': 1, 'x': 0, 'y': 0, 'width': 1, 'id': 89}"))

        r11 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'height': 1, 'x': 0, 'y': 0, 'width': 1, 'id': 89}"))

        r11 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'height': 2, 'x': 0, 'y': 0, 'width': 1, 'id': 89}"))

        r11 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 0, 'width': 1, 'id': 89}"))

        r11= Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(print(r11.to_dictionary()),
            print("{'height': 2, 'x': 3, 'y': 4, 'width': 1, 'id': 89}"))

    def test_rect_save_to_file(self):
        rect_list = None
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        
        r12 = Rectangle(1, 2, 1, 1, 15)
        r13 = Rectangle(3, 4, 2, 2, 16)
        rect_list = [r12, r13]
        Rectangle.save_to_file(rect_list)

        with open("Rectangle.json", "r") as file:
            reader = file.read()
            to_dict = [r12.to_dictionary(), r13.to_dictionary()]
            self.assertEqual(reader, json.dumps(to_dict))

        rect_list = []
        Rectangle.save_to_file(rect_list)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')            

    def test_load_from_file(self):
        r14 = Rectangle(1, 2, 3, 4)
        r15 = Rectangle(5, 6)
        list_rectangles_input = [r14, r15]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(list_rectangles_input[0].to_dictionary(), list_rectangles_output[0].to_dictionary())
        self.assertEqual(list_rectangles_input[1].to_dictionary(), list_rectangles_output[1].to_dictionary())

        try:
            os.remove("Rectangle.json")
        except:
            pass
        finally:
            self.assertEqual(Rectangle.load_from_file(), [])

        try:
            os.remove("Rectangle.json")
        except:
            pass
        with open("Rectangle.json", 'a') as file:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])
