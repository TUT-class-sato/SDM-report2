#!/usr/bin/python3

import re
                
def calc(A,B):
        if "." in str(A) or "." in str(B):#小数を省く
                return -1
        if str(A).startswith('0') or str(B).startswith('0'):#0から始まる文字列を省く
                return -1

        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) and p.match(bi):#両方数値である
                
                a=float(ai)
                b=float(bi)

                if 1<=a<=999 and 1<=b<=999:#両方0~999の範囲に
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

