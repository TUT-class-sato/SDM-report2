#!/usr/bin/python3

import re


def calc(A, B):
    regobj = re.compile("^[0-9]+$")
    if regobj.match(str(A)) and regobj.match(str(B)):
        A = int(A)
        B = int(B)
        if (min(A, B) > 0) and (max(A, B) < 1000):
            return A * B
        else:
            return -1
    else:
        return -1


def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
    main()
