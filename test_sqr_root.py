# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:24:21 2022

@author: Jay Gautam
"""
## Math rules to find square root.
    # 1. number should be positive or zero.
    # 2. number should be int or float.
    # 3. number should not be negative.
## You can add more test cases-> Ex- unequal test cases.

import unittest
from sqr_root import sqr_root_num

class TestSqrRoot(unittest.TestCase):
    def test_sqr_root_number_is_int(self):
        self.assertEqual(sqr_root_num(2), 1.414)
        
    def test_sqr_root_number_is_float(self):
        self.assertEqual(sqr_root_num(9.5), 3.082)
        
    def test_sqr_root_number_is_string(self):
        with self.assertRaises(TypeError):
            sqr_root_num('Two')
        
    def test_sqr_root_number_in_list_format(self):
        with self.assertRaises(TypeError):
            sqr_root_num([])
            
    def test_sqr_root_negative_number(self):
        with self.assertRaises(TypeError):
            sqr_root_num(-3)
    
if __name__ == '__main__':
    unittest.main()