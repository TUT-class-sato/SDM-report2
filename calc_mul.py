#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        #p = re.compile('\d+(\.\d+)?') #original
        p = re.compile('\d+')
        #if p.match(ai) or p.match(bi): #original
        if p.match(ai) and p.match(bi) and '.' not in ai and '.' not in bi: 
                a=float(ai)
                b=float(bi)
                if 1<=a and 1<=b and a<=999 and b<=999: #revised
                #if 0<a and a<b and b<1000: #original
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                print("ans: ", ans)
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
