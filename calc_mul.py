#!/usr/bin/python3

import re


def calc(A, B):
    # 入力が有効であるかを判定
    if isValidInteger(str(A)) and isValidInteger(str(B)):
        return int(A)*int(B)
    else:
        return -1


# 引数が有効な数字であるかを判定する関数
def isValidInteger(input):
    if (input.isdecimal() and input[0] != "0"):
        input = int(input)
        if (input > 0) and (input < 1000):
            return True
        else:
            return False
    else:
        return False


def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
    main()
