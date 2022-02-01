#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('(\d+)*')#<正規表現の変更
        if p.fullmatch(ai) and p.fullmatch(bi):#<文字列全体のマッチング
                a=float(ai)
                b=float(bi)
                if 0<a and a<1000 and 0<b and b<1000:#<入力の定義域の変更
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
