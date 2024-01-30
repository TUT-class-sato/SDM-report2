#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^\d+$') # 正則表現を修正
        if p.match(ai) and p.match(bi):
                a=int(ai) # 整数以外は入力されないためfloat型からint型に変更
                b=int(bi)
                if 0<a<1000 and 0<b<1000:  # 論理演算をorからand二変更、大小比較を削除
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
