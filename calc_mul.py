#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+$') #正規表現を整数のみに変更
        if p.match(ai) and p.match(bi): #論理積を取るように変更
                a=int(ai)
                b=int(bi)
                if (0<a and a<1000) and (0<b and b<1000): # a < bの条件を除去
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
