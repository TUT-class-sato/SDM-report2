#!/usr/bin/python3

import re
import unicodedata


def calc(A, B):
    ai = str(A)
    bi = str(B)
    floatable = re.compile('^\d+(\.\d+)?$')
    # consider also "?a:" ASCII flag ('\d' match only ASCII,
    # not any char from Unicode category 'Number digit' [Nd])
    if floatable.match(ai) and floatable.match(bi):
        a = float(ai)
        b = float(bi)
        in_range = (1 <= a <= 999) and (1 <= b <= 999)
        integers = (a == float(int(a))) and (b == float(int(b)))
        valid = in_range and integers
    else:
        valid = False
    if valid:
        ans = a * b
        return ans
    else:
        return -1


def normalize(str_with_unicode_digits):
    digit = re.compile('\d')
    chars = [str(int(unicodedata.numeric(ch))) if digit.match(ch)
             else ch
             for ch in str_with_unicode_digits]
    str_with_ascii_digits = "".join(chars)
    return str_with_ascii_digits


def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
    main()
