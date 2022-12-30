#!/usr/bin/python3
"""
Unittest for max_integer([])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_unsigned_int_and_float(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([76, 56, 74]), 76)
        self.assertEqual(max_integer([50, 50, 50]), 50)
        self.assertEqual(max_integer([56, 98, 100]), 100)
        self.assertEqual(max_integer([12, 13, 11]), 13)
        self.assertEqual(max_integer([12.3, 45.6, 6.7]), 45.6)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
    
    def test_signed_int_and_float(self):
        self.assertEqual(max_integer([-3.0, -5, 7.5]), 7.5)
        self.assertEqual(max_integer([-3.5, -7.4, -0.3]), -0.3)
        self.assertEqual(max_integer([-0.0, -0.1, -0.2, 0.0]), 0.0)

    def test_string(self):
        self.assertEqual(max_integer(["768", "345", "657", "890"]), '890')
        self.assertEqual(max_integer(["abc", "z"]), 'z')
        self.assertEqual(max_integer(["a", "b", "z", "g"]), 'z')
        self.assertEqual(max_integer("abcnd"), 'n')

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_for_error_type(self):
        with self.assertRaises(TypeError):
            max_integer({1,2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([1, 3, 4, {2, 4}])
        with self.assertRaises(TypeError):
            max_integer([-45, 7.4, "hello"])

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]), [9, 0])
        

