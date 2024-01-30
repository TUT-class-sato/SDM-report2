#!/usr/bin/python3

import unittest
import unicodedata
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


        def test_sample_add(self):
                TH=[100,1,999]
                FsH=[0,1000,10000,-100,0.5]
                FsZ=["１００","-１００","１００００","０","１","９９９","１０００","１０^２","０.５","10^2"]
                Fm =["ｔｓｔ","tst"]
                ##K*Mが上手く行えない

   
                for k in TH:
                        for m in TH:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(k*m,calc(k,m),f"assert error T->F{sum}")
                
                for k in TH:
                        for m in FsH:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")
                                
                                        

                for k in TH:
                        for m in FsZ:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")
                                        

                for k in TH:
                        for m in Fm:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")
                                        
                for k in FsH:
                        for m in FsH:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")

                for k in FsH:
                        for m in FsZ:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")
                
                for k in FsH:
                        for m in Fm:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")
      
                for k in FsZ:
                        for m in FsZ:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}") 

                for k in FsZ:
                        for m in Fm:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")

                for k in Fm:
                        for m in Fm:
                                sum = [k,m]
                                with self.subTest(k=k,m=m):
                                        self.assertEqual(-1,calc(k,m),f"assert error F->T{sum}")
