#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\d+)?') #整数だけ
        if p.match(ai) and p.match(bi): #change "or" to "and"
                a=float(ai)
                b=float(bi)
                # 1<= a <= 999 & 1<= b <= 999
                if 1<= a and a <=999 and 1 <= b and b<=999: 
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
