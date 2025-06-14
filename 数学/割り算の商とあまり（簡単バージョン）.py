# 割り算の商とあまり（簡単バージョン）

print("A ÷ B = ?")
A = int(input("Aを入力："))
B = int(input("Bを入力："))

if B == 0:
    raise ValueError("ゼロで割ることはできません。")

print("{} ÷ {} = {} あまり {}".format(A, B, A // B, A % B))