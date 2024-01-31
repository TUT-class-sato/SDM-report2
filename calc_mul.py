#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) or p.match(bi):

                try:#整数か小数かその他かを見分ける
                        a = float(ai)
                        b = float(bi)
                        if a.is_integer() and b.is_integer():
                                #整数
                                if 0 < a and a < 1000 and 0 < b and b < 1000:
                                        valid=True
                                else:
                                        valid = False
                        else:
                                #小数
                                valid=False
                except ValueError:
                #その他
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return int(ans)
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
