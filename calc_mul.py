#!/usr/bin/python3

import re
                
def calc(A,B):
        if not((isinstance(A, str) or isinstance(A, int)) \
               and (isinstance(B, str) or isinstance(B, int))):
                valid = False
        elif isinstance(A, str) and A.isalpha() or isinstance(B, str) and B.isalpha(): # 'a'などの16進数は除外
                valid=False
        else:
                ai=str(A)
                bi=str(B)
                p = re.compile('(^\d+$)|(\d+[eE]\d+)') # 整数、指数表記の整数のマッチ
                if p.match(ai) and p.match(bi): # or -> and
                        a=int(float(ai)) # float()は指数表記を数値に変換可能
                        b=int(float(bi))
                        if 0<min(a,b) and max(a,b)<1000:
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
