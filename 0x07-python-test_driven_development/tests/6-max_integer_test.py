#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        
        # Test with a list of positive and negative integers
        self.assertEqual(max_integer([1, 3, 4, 2, -1, -4]), 4)
        
        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
        # Test with an empty list
        self.assertIsNone(max_integer([]))
        
        # Test with a list containing a single element
        self.assertEqual(max_integer([5]), 5)
        
        # Test with a list containing duplicate elements
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()
