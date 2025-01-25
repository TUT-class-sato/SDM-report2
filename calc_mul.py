#!/usr/bin/python3

import re
                
def calc(A,B):
	# 文字列変換
	ai=str(A)
	bi=str(B)
	# 整数データか確認
	p = re.compile('[0-9]+')
	if p.fullmatch(ai) and p.fullmatch(bi):
		a = int(ai)
		b = int(bi)
		# 整数範囲の確認
		if (a > 0 and a < 1000) and (b > 0 and b < 1000):
			valid = True
		else:
			valid = False
	else:
		valid = False

	if valid:
		ans = a * b
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
