# 割り算の商とあまり（難しいバージョン）

print("A ÷ B = ?")
A = int(input("Aを入力："))
B = int(input("Bを入力："))

def f(a, b):
    if B == 0:
        raise ValueError("ゼロで割ることはできません。")
    x = 0
    while a >= b:
        a -= b
        x += 1
    return x, a

c, d = f(A, B)

print("{} ÷ {} = {} あまり {}".format(A, B, c, d))