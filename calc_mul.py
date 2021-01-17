#!/usr/bin/python3

# 正規表現を扱うライブラリ
import re


def calc(A, B):
    ai = str(A)
    bi = str(B)

    # 正規表現パターンオブジェクトの生成
    # 入力が整数の場合にマッチ
    p = re.compile('^(?=.*\d)(?!.*\.).*$')

    # 入力が条件を満たすかの判定
    if p.match(ai) and p.match(bi):  # pに対してaiとbiがマッチするとき
        a = float(ai)
        b = float(bi)
        # 数字の大きさ判定
        if 0 < a and b < 1000:
            valid = True
        else:
            valid = False
    else:
        valid = False
    # 判定による処理
    if valid:
        # 入力の積を返す
        ans = a*b
        return ans
    else:
        # -1を返す
        return -1


def main():
    matchstring = ''
    while matchstring != 'end':
        # 標準入力からのA,B読み取り
        A = input('input A: ')
        B = input('input B: ')

        # 結果の表示
        print('input A * input B = ', calc(A, B))


# メイン文の実行
if __name__ == '__main__':
    main()
