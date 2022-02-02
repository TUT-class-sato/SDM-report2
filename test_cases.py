#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # a,b are integers and in range [1,999], a < b
        def test_sample01 (self):
                self.assertEqual (21, calc(3,7))

        # a,b are integers, a < 1, b in range [1,999]
        def test_sample02 (self):
                self.assertEqual (-1, calc(0,150))

        # a, b is both string
        def test_sample03 (self):
                self.assertEqual (-1, calc('a','b'))

        # a is float, a < 1 and also a non-negative number
        # b is integer in range [1, 999]
        def test_sample04 (self):
                self.assertEqual (-1, calc(0.1,999))

        # a,b are integers, a in range [1,999]
        # b < 1 and also non-negative number
        def test_sample05 (self):
                self.assertEqual(-1,calc(1,-35))

        # a,b are integers, a in range [1,999]
        # b < 1 and also negative number
        def test_sample06 (self):
                self.assertEqual(-1,calc(1,0.5))

        # a,b are integers, a in range [1,999], b > 999
        def test_sample07 (self):
                self.assertEqual(-1,calc(1,1234))

        # a is integer and in range [1,999]
        # b is float and in range [1,999]
        def test_sample08 (self):
                self.assertEqual(-1,calc(1,23.5))

        #  a is integer and in range [1,999]
        #  b is float, b < 1 and also negative number
        def test_sample09 (self):
                self.assertEqual(-1,calc(1,-0.5))

        #  a is integer and in range [1,999]
        #  b is float, b < 1 and also non-negative number
        def test_sample10 (self):
                self.assertEqual(-1,calc(1,0.5))

        #  a is integer and in range [1,999]
        #  b is float and b > 999
        def test_sample11 (self):
                self.assertEqual(-1,calc(1,999.5))

        # a,b are integers 
        # a < 1 and also non-negative number
        # b in range [1,999]
        def test_sample12 (self):
                self.assertEqual (-1, calc(0.1,7))

        # a,b are integers
        # a < 1 and also negative-number
        # b in range [1,999]
        def test_sample13 (self):
                self.assertEqual (-1, calc(-3.1,7))

        # a,b are integers, a > 999, b in range [1,999]
        def test_sample14 (self):
                self.assertEqual (-1, calc(1023,7))

        # a is float and in range [1,999]
        # b is integer and in range [1,999]
        def test_sample15 (self):
                self.assertEqual(-1,calc(22.6,1))   

        # a is float, a < 1 and also a negative number
        # b is integer and in range [1,999]
        def test_sample16 (self):
                self.assertEqual(-1,calc(-2.6,1))   

        # a is float in range [1,999]
        # b is integer and in range [1,999]
        def test_sample17 (self):
                self.assertEqual(-1,calc(1.6,1))  

        # a is float and a > 999
        # b is integer and in range [1,999]
        def test_sample18 (self):
                self.assertEqual(-1,calc(1234.6,1))   

        # a,b are floats and in range [1,999]
        def test_sample19 (self):
                self.assertEqual(-1,calc(5,8.9))   

        # a,b are integers and in range [1,999], a > b
        def test_sample20 (self):
                self.assertEqual(117,calc(39,3))

        # a,b are integers and a,b in range [1,999], a = b
        def test_sample21 (self):
                self.assertEqual(7744,calc(88,88))

        # a is integer in range [1,999], b is string 
        def test_sample22 (self):
                self.assertEqual(-1,calc(8,"somestring"))

        # a is string, b is integer in range [1,999]
        def test_sample23 (self):
                self.assertEqual(-1,calc("somestring",1))
   
 

