#!/usr/bin/python3

import re
                
def calc(A,B):
        valid=True
        ai=str(A)
        bi=str(B)
        p = re.compile('^([1-9][0-9]{0,2})$')
        if p.fullmatch(ai) and p.fullmatch(bi):
                a=int(ai)#floatからintに変更
                b=int(bi)
                if (not(a > 0 and a < 1000) or not(b > 0 and b < 1000)) : #a>bを受け付けないバグを修正
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
