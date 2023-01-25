#!/usr/bin/python3

import re

def calc(A, B):
    valid = False
    if isinstance(A, int) and isinstance(B, int):
        if (1 <= A <= 999) and (1 <= B <= 999):
            valid=True

    ans = -1
    if valid:
        ans = A * B

    return ans


def main ():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
    main()
