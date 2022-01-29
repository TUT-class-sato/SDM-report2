#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # 有効同値 1から999の整数
        def test_accept1(self):
                self.assertEqual(250000,calc(500,500))

        def test_accept2(self):
                self.assertEqual(999,calc(1,999))

        def test_accept3(self):
                self.assertEqual(999,calc(999,1))
        
        # 無効同値 1未満の整数
        def test_lowerbound1(self):
                self.assertEqual(-1,calc(0,1))
        
        def test_lowerbound2(self):
                self.assertEqual(-1,calc(-1,1))
        
        # 無効同値 1未満の小数
        def test_lowerbound3(self):
                self.assertEqual(-1,calc(0.9,1))
        
        def test_lowerbound4(self):
                self.assertEqual(-1,calc(-0.9,1))
        
        # 無効同値 999より大きい整数
        def test_upperbound1(self):
                self.assertEqual(-1,calc(1,1000))

        def test_upperbound2(self):
                self.assertEqual(-1,calc(1,1001))
        
        # 無効同値 999より大きい小数
        def test_upperbound3(self):
                self.assertEqual(-1,calc(1,999.9))
                
        def test_upperbound4(self):
                self.assertEqual(-1,calc(1,1000.1))
        
        # 無効同値 1から999までの小数
        def test_decimal(self):
                self.assertEqual(-1,calc(1.1,998.9))

        # 無効同値 数値ではない入力
        def test_non_numeric1(self):
                self.assertEqual(-1,calc('str',1))

        def test_non_numeric2(self):
                self.assertEqual(-1,calc('str','c'))

        def test_non_numeric3(self):
                self.assertEqual(-1,calc('1',999))

        def test_non_numeric4(self):
                self.assertEqual(-1,calc('1','999'))

        def test_non_numeric5(self):
                self.assertEqual(-1,calc('1.1','998.9'))
        
        # 無効同値 値の非存在を表すNone(数値ではない入力)
        def test_non_numeric6(self):
                self.assertEqual(-1,calc(None,999))
                
        def test_non_numeric7(self):
                self.assertEqual(-1,calc(1,None))

        def test_non_numeric8(self):
                self.assertEqual(-1,calc(None,None))
        