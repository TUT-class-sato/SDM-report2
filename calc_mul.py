#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
	#入力された文字列が整数のみであることを確認
        p = re.compile('\d+$')
	#ai,biがどちらも整数であることの確認
        if p.match(ai) and p.match(bi):
                a=float(ai)
                b=float(bi)
	#a, bの範囲を1～999にする
                if (0<a and a<1000)and(0<b and b<1000):
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
