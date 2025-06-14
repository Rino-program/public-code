# 自然数チェッカー
x = input("数を入力")
try:
    x = float(x)
    if x < 0:
        print("負の数です。")
    else:
        if int(x) == x:
            print("自然数です。")
        else:
            print("正の少数です。")
except ValueError:
    print("数字ではありません。")
