
#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):
    
    def parameterized_test(self, input1, input2, expected_result):
        self.assertEqual(expected_result, calc(input1, input2))

# Define the input matrix
test_data = [
    # accept: 1~999, 整数, 数値
    # not accept: x<1, x>999, 小数, char
    (3, 7, 21), #accept
    (7, 3, 21), #order is reversed
    (999, 1000, -1), #out of boundary
    (0, 1, -1), #out of boundary
    ('a', 1, -1), #one side is charactors
    ("a", '.', -1), #both are charactors
    (1.1, 10, -1), #one is decimal
    (1.1, 2.2, -1), #both are decimal
    (0.9, 999.1, -1), #decimal near the boundary
    # Add more test cases as needed
]

# Generate test methods dynamically based on the input matrix
for i, (input1, input2, expected_result) in enumerate(test_data):
    test_method_name = f'test_case_{i + 1}'
    setattr(TestCalc, test_method_name, lambda self, input1=input1, input2=input2, expected_result=expected_result: self.parameterized_test(input1, input2, expected_result))

if __name__ == '__main__':
    unittest.main()