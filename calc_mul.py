def calc(A, B):
    try:
        a = int(A)
        b = int(B)
        if 1 <= a <= 999 and 1 <= b <= 999:
            return a * b
        else:
            return -1
    except ValueError:
        return -1


def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
    main()
