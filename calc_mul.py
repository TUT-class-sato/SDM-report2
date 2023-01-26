#!/usr/bin/python3

import re

def calc(A, B):
    ans = -1
    if isinstance(A, int) and isinstance(B, int):
        if (1 <= A <= 999) and (1 <= B <= 999):
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
