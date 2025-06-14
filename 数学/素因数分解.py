# 素因数分解
from math import sqrt

def m(x):
    # 素因数分解
    # 1. 2で割り切れるだけ割る
    while x % 2 == 0:
        print(2, end=' ')
        x //= 2
    # 2. 奇数で割り切れるだけ割る
    for i in range(3, int(sqrt(x)) + 1, 2):
        while x % i == 0:
            print(i, end=' ')
            x //= i
    # 3. 残った数が素数なら出力する
    if x > 1:
        print(x, end=' ')

if __name__ == '__main__':
    m(int(input("数字を入力:")))