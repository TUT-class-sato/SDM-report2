#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #1 Correct Input
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        #2 Incorrect A since A=0<1
        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        #3 Incorrect B input since B<1 
        def test_added1 (self):
                self.assertEqual (-1, calc(100,0))
        
        #3 Incorrect A and B input since both are <1 
        def test_added2 (self):
                self.assertEqual (-1, calc(0,0))
        
        #4 Incorrect A since A=1000>999
        def test_added3 (self):
                self.assertEqual (-1, calc(1000,150))

        #5 Incorrect B input since B=1200>999 
        def test_added4 (self):
                self.assertEqual (-1, calc(190,1200))

        #6 Incorrect A and B input since both are >999 
        def test_added5 (self):
                self.assertEqual (-1, calc(1000,1200))
        
        #8 Incorrect since A and B since both are not integer (strings)
        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        #8 Incorrect since B is not integer (strings)
        def test_added6 (self):
                self.assertEqual (-1, calc(90,'b'))

        #7 Incorrect since A is not integer (strings)
        def test_added7 (self):
                self.assertEqual (-1, calc('a',26))

        #8 incorrect A input since 0.1 is not Integer(Floating-point number)
        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        #9 incorrect B input since 7.5 is not Integer(Floating-point number)
        def test_added8 (self):
                self.assertEqual (-1, calc(56, 7.5))

        #10 incorrect A and B input since both are not Integer(Floating-point number)
        def test_added9 (self):
                self.assertEqual (-1, calc(9.6,88.3))

        #単体テストのコツから
        # TestEdge Cases 
        #11 Correct 1 = 1*1
        def test_tips1 (self):
                self.assertEqual (1, calc(1,1))
        
        #12 Correct 998001 = 999*999
        def test_tips1b (self):
                self.assertEqual (998001, calc(999,999))

        #13 Correct 999 = 1*999
        def test_tips1c (self):
                self.assertEqual (999, calc(1,999))

        # Repeat yourself cases
        def test_tips2 (self):
                self.assertEqual (295936, calc(544,544))

        def test_tips2b (self):
                self.assertEqual (5929, calc(77,77))

        def test_tips2c (self):
                self.assertEqual (81, calc(9,9))

        # Keep Count cases
        def test_tips3 (self):
                self.assertEqual (90, calc(9,10))

        def test_tips3b (self):
                self.assertEqual (90, calc(9,10))

        def test_tips3c (self):
                self.assertEqual (90, calc(9,10))
        
        # Don't forget Null and zero
        def test_tips4(self):
                self.assertEqual (-1, calc (0,0))

        def test_tips4b(self):
                self.assertEqual (-1, calc (4,None))

        def test_tips4c(self):
                self.assertEqual (-1, calc (None,6))
        
        def test_tips4d(self):
                self.assertEqual (-1, calc (None,None))

        # Extreme Underflow and Overflow
        def test_tips5(self):
                self.assertEqual (-1, calc (123145325,12))
        
        def test_tips5b(self):
                self.assertEqual (-1, calc (12,124564356))
        
        def test_tips5c(self):
                self.assertEqual (-1, calc (123125,45645542))
        


        

