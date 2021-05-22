#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class of tests for max_integer function"""

    def test_zero(self):
        """tests for results"""
        self.assertAlmostEqual(max_integer([0, 0, 0, 0]), 0)

    def test_null(self):
        """check if null"""
        self.assertAlmostEqual(max_integer([]), None)

    def test_one_element(self):
        """check if there is only one element"""
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_return(self):
        """test return value"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negativ(self):
        """test with negative value"""
        self.assertAlmostEqual(max_integer([-1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, -2, -3, 0]), 0)

    def test_float(self):
        """test with float value"""
        self.assertAlmostEqual(max_integer([1.1, 2.2, 3.3, 4.0]), 4.0)

    def test_not_num(self):
        """test with only string"""
        self.assertAlmostEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
