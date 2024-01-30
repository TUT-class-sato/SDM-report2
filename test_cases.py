#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

        # 同値分割法: 正の整数         
        def test_positive_numbers_1(self):
                self.assertEqual(15, calc(3, 5))
        def test_positive_numbers_2(self):
                self.assertEqual(200, calc(20, 10))
        def test_positive_numbers_3(self):
                self.assertEqual(999 * 999, calc(999, 999))
        
        # 同値分割法: 負の整数
        def test_negative_numbers_1(self):
                self.assertEqual(-1, calc(-1, 100))
        def test_negative_numbers_2(self):
                self.assertEqual(-1, calc(100, -1))
        def test_negative_numbers_3(self):
                self.assertEqual(-1, calc(-1, -1))
                
        # 同値分割法: 無効な入力 (非整数)
        def test_invalid_inputs_1(self):
                self.assertEqual(-1, calc('a', 5))
        def test_invalid_inputs_2(self):
                self.assertEqual(-1, calc(3, 'b'))
        def test_invalid_inputs_3(self):
                self.assertEqual(-1, calc('x', 'y'))
                
        # 同値分割法: 浮動小数点数の入力
        def test_float_inputs_1(self):
                self.assertEqual(-1, calc(0.1, 999))
        def test_float_inputs_2(self):
                self.assertEqual(-1, calc(999, 0.1))
        def test_float_inputs_3(self):
                self.assertEqual(-1, calc(0.1, 0.1))
                
        # 境界値分割法: 入力の境界値
        def test_boundary_values_1(self):
                self.assertEqual(1, calc(1, 1))
        def test_boundary_values_2(self):
                self.assertEqual(999 * 999, calc(999, 999))
        def test_boundary_values_3(self):
                self.assertEqual(-1, calc(0, 1))
        def test_boundary_values_4(self):
                self.assertEqual(-1, calc(1, 0))
        def test_boundary_values_5(self):
                self.assertEqual(-1, calc(1000, 999))
        def test_boundary_values_6(self):
                self.assertEqual(-1, calc(999, 1000))

