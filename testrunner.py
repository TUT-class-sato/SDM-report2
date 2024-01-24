#!/usr/bin/python3

import unittest
import sys

loader = unittest.TestLoader()


#Find the test files in the current directory
# tests = loader.discover('.')

# テスト対象のファイル名を指定
test_module_name = 'test_cases2'

# ファイル名からテストをロード
tests = loader.loadTestsFromName(test_module_name)

#Specify the level of information provided by the test runner

testRunner = unittest.runner.TextTestRunner(verbosity=2)

results=testRunner.run(tests)

#print( "results: %s" % results )
#print( "results.wasSuccessful: %s" % results.wasSuccessful() )
if results.wasSuccessful()==False:
    sys.exit(1)

