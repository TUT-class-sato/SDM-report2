#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

                def test1 (self):
                    self.assertEqual (999, calc(1,999))
                
                def test2 (self):
                    self.assertEqual (15, calc(3,5))     
                
                def test3 (self):
                    self.assertEqual (-1, calc(0.1,5))

                def test4 (self):
                    self.assertEqual (-1, calc('a',5))

                def test5 (self):
                    self.assertEqual (-1, calc("STR",3))
                
                def test6 (self):
                    self.assertEqual (-1, calc("A1",3))
                
                def test7 (self):
                    self.assertEqual (-1, calc(1000,3))

                def test8 (self):                                                                                                           self.assertEqual (-1, calc(5,-1))

                def test9 (self):                                                                                                           self.assertEqual (-1, calc(0,3))

                def test10 (self):                                                                                                           self.assertEqual (-1, calc(0.1,0.1))

                def test11(self):
                    self.assertEqual(-1,calc('A','B'))
                
                def test12(self):
                    self.assertEqual(-1,calc('A',0.1))

                def test13(self):
                    self.assertEqual (-1, calc("1A",3)) 

                def test14(self):
                    self.assertEqual (15, calc(5,3)) 
