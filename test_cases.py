#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

    # 同値分割法: 有効な値の場合
    def test_valid_cases(self):
        # 最小の有効値
        self.assertEqual(calc(1, 1), 1)         
        # 最大の有効値
        self.assertEqual(calc(999, 999), 998001)
        # 中間の有効値
        self.assertEqual(calc(10, 20), 200)    

    # 境界値分析: 境界値と境界外の値
    def test_boundary_cases(self):
        # 境界値
        self.assertEqual(calc(1, 999), 999)    # 境界値
        self.assertEqual(calc(999, 1), 999)    # 境界値
        # 境界外（下限）
        self.assertEqual(calc(0, 999), -1)     
        # 境界外（上限）
        self.assertEqual(calc(1, 1000), -1)    

    # 同値分割法: 範囲外の値
    def test_out_of_range(self):
        # 負の数
        self.assertEqual(calc(-1, 500), -1)    
        # 上限超え
        self.assertEqual(calc(500, 1000), -1)  

    # エラーハンドリング: 無効な入力（浮動小数点、文字列）
    def test_invalid_inputs(self):
        # 浮動小数点数
        self.assertEqual(calc(0.5, 500), -1)   
        # 文字列
        self.assertEqual(calc(500, "abc"), -1) 
        # 両方文字列
        self.assertEqual(calc("xyz", "abc"), -1)
        # 数値文字列
        self.assertEqual(calc("100", 500), -1) 

