#!/usr/bin/python3

import re
                
def calc(A,B):
        # ai=str(A)
        # bi=str(B)
        # p = re.compile('\d+(\.\d+)?')
        # if p.match(ai) or p.match(bi):
        #         a=float(ai)
        #         b=float(bi)
        #         if 0<a and a<b and b<1000:
        #                 valid=True
        #         else:
        #                 valid=False
        # else:
        #         valid=False
                
        # if valid:
        #         ans=a*b
        #         return ans
        # else:
        #         return -1

        # 正規表現用
        ai = str(A)
        bi = str(B)
        p = re.compile('[0-9０-９]+')

        valid = True
        # 小数，数字以外の文字列でないか
        if p.fullmatch(ai) and p.fullmatch(bi):
                # 指定範囲内（1~999）でないか
                a = int(ai)
                b = int(bi)
                if (not (a >= 1 and a <= 999)) or (not (b >= 1 and b <= 999)):
                        valid = False
        else:
                valid = False

        if valid:
                return a * b
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
