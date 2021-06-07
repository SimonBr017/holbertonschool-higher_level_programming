#!/usr/bin/python3
"""Unit test for module base"""

from models.base import Base
import unittest


class BaseTests (unittest.TestCase):
    """Test for class base"""
    
    def test_baseId(self):
        """tests for class base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)
        
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        
        b5 = Base()
        self.assertEqual(b5.id, 4)
    
    def test_json_to(self):
        """test for to_json"""
        json_s = Base.to_json_string(None)
        self.assertEqual(json_s, "[]")
        