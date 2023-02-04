#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) or p.match(bi):
                a=float(ai)
                b=float(bi)
                try:
                        int(ai)  # 文字列を実際にint関数で変換してみる
                except ValueError:
                        a_int_test = False
                else:
                        a = int(ai)
                        a_int_test = True
                try:
                        int(bi)  # 文字列を実際にint関数で変換してみる
                except ValueError:
                        b_int_test = False
                else:
                        b = int(bi)
                        b_int_test = True
         
                if a_int_test and b_int_test:
                        if (0<a and a<1000 and 0<b and b<1000):
                                valid=True
                        else:
                                valid=False
                else:
                        valid = False
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
