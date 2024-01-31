#!/usr/bin/python3

def calc(A,B):
    if type(A) is int and type(B) is int and 0 < A and A < 1000 and 0 < B and B < 1000:
        return A*B
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
