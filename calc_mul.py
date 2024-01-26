#!/usr/bin/python3

import re
                
def calc(A, B):
    # 文字列に変換
    ai = str(A)
    bi = str(B)
    # 数値のみの文字列かどうかをチェック
    p = re.compile('[0-9０-９]+')
    if p.fullmatch(ai) and p.fullmatch(bi):
        a = int(ai)
        b = int(bi)
        # １以上９９９以下の範囲のチェック
        if (a >= 1 and a <= 999) and (b >= 1 and b <= 999):
            valid = True
        else:
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
