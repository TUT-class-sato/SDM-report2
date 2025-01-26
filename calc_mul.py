#!/usr/bin/python3

import re
                
"""def calc(A, B):
        # AとBが整数であるかを確認
        if isinstance(A, int) and isinstance(B, int):
                # 1 <= A, B <= 999 の範囲であるかを確認
                if 1 <= A <= 999 and 1 <= B <= 999:
                        return A * B
                else:
                        return -1
        else:
                return -1"""
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) or p.match(bi):
                a=float(ai)
                b=float(bi)
                if 0<a and a<b and b<1000:
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
