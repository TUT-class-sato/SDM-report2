import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_case1 (self):
                self.assertEqual (45, calc(5,9))

        def test_case2 (self):
                self.assertEqual (45, calc(9,5))

        def test_case3 (self):
                self.assertEqual (100, calc(10,10))
        
        def test_case4 (self):
                self.assertEqual (-1, calc(0.99,100))
        
        def test_case5 (self):
                self.assertEqual (-1, calc(10,999.1))
 
        def test_case6 (self):
                self.assertEqual (-1, calc(0.01,999.9))

        def test_case7 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_case8 (self):
                self.assertEqual (-1, calc('a',500))