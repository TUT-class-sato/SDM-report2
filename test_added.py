
import unittest
from calc_mul import calc

class  TestCalc (unittest.TestCase):

    def test_case1 (self):
        self.assertEqual (1, calc(1,1))

    def test_case2 (self):
        self.assertEqual (999, calc(1,999))

    def test_case3 (self):
        self.assertEqual (-1, calc(1,0))

    def test_case4 (self):
        self.assertEqual (-1, calc(1,1000))

    def test_case5 (self):
        self.assertEqual (-1, calc(1,0.999))

    def test_case6 (self):
        self.assertEqual (-1, calc(1,999.001))

    def test_case7 (self):
        self.assertEqual (-1, calc(1,"a"))

    def test_case8 (self):
        self.assertEqual (999, calc(999,1))

    def test_case9 (self):
        self.assertEqual (998001, calc(999,999))

    def test_case10 (self):
        self.assertEqual (-1, calc(999,0))

    def test_case11 (self):
        self.assertEqual (-1, calc(999,1000))

    def test_case12 (self):
        self.assertEqual (-1, calc(999,0.999))

    def test_case13 (self):
        self.assertEqual (-1, calc(999,999.001))

    def test_case14 (self):
        self.assertEqual (-1, calc(999,"a"))

    def test_case15 (self):
        self.assertEqual (-1, calc(0,1))

    def test_case16 (self):
        self.assertEqual (-1, calc(0,999))

    def test_case17 (self):
        self.assertEqual (-1, calc(0,0))

    def test_case18 (self):
        self.assertEqual (-1, calc(0,1000))

    def test_case19 (self):
        self.assertEqual (-1, calc(0,0.999))

    def test_case20 (self):
        self.assertEqual (-1, calc(0,999.001))

    def test_case21 (self):
        self.assertEqual (-1, calc(0,"a"))

    def test_case22 (self):
        self.assertEqual (-1, calc(1000,1))

    def test_case23 (self):
        self.assertEqual (-1, calc(1000,999))

    def test_case24 (self):
        self.assertEqual (-1, calc(1000,0))

    def test_case25 (self):
        self.assertEqual (-1, calc(1000,1000))

    def test_case26 (self):
        self.assertEqual (-1, calc(1000,0.999))

    def test_case27 (self):
        self.assertEqual (-1, calc(1000,999.001))

    def test_case28 (self):
        self.assertEqual (-1, calc(1000,"a"))

    def test_case29 (self):
        self.assertEqual (-1, calc(0.999,1))

    def test_case30 (self):
        self.assertEqual (-1, calc(0.999,999))

    def test_case31 (self):
        self.assertEqual (-1, calc(0.999,0))

    def test_case32 (self):
        self.assertEqual (-1, calc(0.999,1000))

    def test_case33 (self):
        self.assertEqual (-1, calc(0.999,0.999))

    def test_case34 (self):
        self.assertEqual (-1, calc(0.999,999.001))

    def test_case35 (self):
        self.assertEqual (-1, calc(0.999,"a"))

    def test_case36 (self):
        self.assertEqual (-1, calc(999.001,1))

    def test_case37 (self):
        self.assertEqual (-1, calc(999.001,999))

    def test_case38 (self):
        self.assertEqual (-1, calc(999.001,0))

    def test_case39 (self):
        self.assertEqual (-1, calc(999.001,1000))

    def test_case40 (self):
        self.assertEqual (-1, calc(999.001,0.999))

    def test_case41 (self):
        self.assertEqual (-1, calc(999.001,999.001))

    def test_case42 (self):
        self.assertEqual (-1, calc(999.001,"a"))

    def test_case43 (self):
        self.assertEqual (-1, calc("a",1))

    def test_case44 (self):
        self.assertEqual (-1, calc("a",999))

    def test_case45 (self):
        self.assertEqual (-1, calc("a",0))

    def test_case46 (self):
        self.assertEqual (-1, calc("a",1000))

    def test_case47 (self):
        self.assertEqual (-1, calc("a",0.999))

    def test_case48 (self):
        self.assertEqual (-1, calc("a",999.001))

    def test_case49 (self):
        self.assertEqual (-1, calc("a","a"))