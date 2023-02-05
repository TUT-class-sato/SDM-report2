#!/usr/bin/python3

import re

def calc(A,B):
        ai=str(A)
        bi=str(B)
        # 初期コード
        #p = re.compile('\d+(\.\d+)?')
        # 新規コード
        p = re.compile('[0-9０-９]+')

        # 初期コード
        #if p.match(ai) or p.match(bi):
        # 新規コード
        if p.fullmatch(ai) and p.fullmatch(bi):
                a=float(ai)
                b=float(bi)
                # 初期コード
                # if 0<a and a<b and b<1000:
                # 新規コード
                if 0<a<1000 and 0<b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False

        if valid:
                ans=a*b
                return ans
        else:
                return -1


def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
