#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # 追加テストケース
        # 1. 有効同値
        # 1.1 範囲に含まれる整数
        # 1.1.1 A>B
        def test_A_lt_B (self):
                self.assertEqual (999, calc(1,999))

        # 1.1.2 B>A
        def test_B_lt_A (self):
                self.assertEqual (999, calc(999,1))

        # 1.1.3 B=A
        def test_B_eq_A (self):
                self.assertEqual (998001, calc(999,999))

        # 1.2 範囲に含まれる整数の文字列
        # 1.2.1 0が先頭にある整数
        def test_str_beginzero (self):
                self.assertEqual (999, calc("001","00999"))

        # 1.2.2 0が先頭にない整数
        def test_str_nobeginzero (self):
                self.assertEqual (999, calc("1","999"))

        # 1.2.3 半角の空白に囲まれる整数
        def test_str_spaceshalffrontA (self):
                self.assertEqual (999, calc("   1","999"))
        def test_str_spaceshalffrontB (self):
                self.assertEqual (999, calc("   1","999"))
        def test_str_spacesbothfront (self):
                self.assertEqual (999, calc("  1","  999"))
        def test_str_spaceshalfbackA (self):
                self.assertEqual (999, calc("1   ","999"))
        def test_str_spaceshalfbackB (self):
                self.assertEqual (999, calc("1","999   "))
        def test_str_spacesbothback (self):
                self.assertEqual (999, calc("1  ","999   "))
        def test_str_spacesfrontback (self):
                self.assertEqual (999, calc("  1  ","  999   "))

        # 1.2.4 半角の空白に囲まれない整数
        def test_str_nospaces (self):
                self.assertEqual (19960, calc("20","998"))
        # 1.2.5 0が先頭にあって、スペースで囲まれる整数
        def test_str_zero_and_spaces (self):
                self.assertEqual (19960, calc("00020","  998")) 
        # 1.3 一方が1.1、もう一方が1.2
        def test_half_numstr (self):
                self.assertEqual (19960, calc(20,"998"))
        def test_half_strnum (self):
                self.assertEqual (19960, calc("20",998))
        def test_half_zeropacesnum (self):
                self.assertEqual (19960, calc("  00020  ",998))

        # 2. 無効同値
        # 2.1 整数ではない文字列
        # 2.1.1 アルファベット
        def test_str_alpha (self):
                self.assertEqual (-1, calc("abc","cde"))

        # 2.1.2 記号
        def test_str_symbol (self):
                self.assertEqual (-1, calc("???","***][[]]"))
       
        # 2.1.3 実数
        def test_str_realnum (self):
                self.assertEqual (-1, calc("3.141592654","999.000000000000000000898954"))
        def test_str_realnumB (self):
                self.assertEqual (-1, calc("1","999.000000000000000000898954"))
        # 2.1.4 アルファベットと記号
        def test_str_alpha_and_symbol1 (self):
                self.assertEqual (-1, calc("ab.c","c.de"))
        def test_str_alpha_and_symbol2 (self):
                self.assertEqual (-1, calc("abc//__",'" or ""="'))

        # 2.2 範囲に含まれない整数
        # 2.2.1 Aのみ
        def test_int_Aoutofbounds (self):
                self.assertEqual (-1, calc(1000, 1))
        def test_int_Aoutofbounds2 (self):
                self.assertEqual (-1, calc(9223372036854775807, 1)) # これはsys.maxsize

        # 2.2.2 Bのみ
        def test_int_Boutofbounds (self):
                self.assertEqual (-1, calc(1, 1000))
        def test_int_Boutofbounds2 (self):
                self.assertEqual (-1, calc(1, 9223372036854775807)) # これはsys.maxsize

        # 2.2.3 AとB
        def test_int_ABoutofbounds (self):
                self.assertEqual (-1, calc(1000, 1000))
        def test_int_ABoutofbounds2 (self):
                self.assertEqual (-1, calc(9223372036854775807, 9223372036854775807)) # これはsys.maxsize

        # 2.3 範囲に含まれない整数の文字列
        # 2.3.1 Aのみ
        def test_str_Aoutofbounds (self):
                self.assertEqual (-1, calc("1000", "1"))
        def test_str_Aoutofbounds2 (self):
                self.assertEqual (-1, calc("9223372036854775807", "1")) # これはsys.maxsize

        # 2.3.2 Bのみ
        def test_str_Boutofbounds (self):
                self.assertEqual (-1, calc("1", "1000"))
        def test_str_Boutofbounds2 (self):
                self.assertEqual (-1, calc("1", "9223372036854775807")) # これはsys.maxsize

        # 2.3.3 AとB
        def test_str_ABoutofbounds (self):
                self.assertEqual (-1, calc("1000", "1000"))
        def test_str_ABoutofbounds2 (self):
                self.assertEqual (-1, calc("9223372036854775807", "9223372036854775807")) # これはsys.maxsize

