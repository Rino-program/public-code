# ガウス
x = input("数を入力")
try:
    x = float(x)
    if x > 0:
        x = int(x)
    else:
        if int(x) != x:
            x = int(x) - 1
        else:
            x = int(x)
    print(x)
except ValueError:
    print("エラー")
