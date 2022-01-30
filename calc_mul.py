#!/usr/bin/python3

import re
                
def calc(A,B):

        # 与えられた値が文字の時, エラー
        if type(A) is str or type(B) is str:
                return -1
        
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+') # \d : 全ての数字
        
        # pの正規表現に完全マッチするとき 
        if p.fullmatch(ai) and p.fullmatch(bi):
                a=float(ai)
                b=float(bi)
                if 1<=a and a<=999 and 1<=b and b<=999:
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
