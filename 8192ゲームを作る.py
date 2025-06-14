# 8192ゲームを作る
# 1/2を13回当てるゲーム
from random import randint as ran
print("8192ゲーム\n1/2を13回当てるゲームだよ。")
count = 0
while True:
    print(f"{count+1}回目。\nあと{13-count}回です。\n当てれる確率は 1/{2**(count+1)} です。")
    i = input("青か緑を入力してください。(0 or 1 でも可)")
    x = ran(0, 1)
    if count == 0 and 2468 == ran(1,8192):
        print("あなたは8192分の1を当てました!(裏ルート)")
        break
    if i == "青" or 0:
        i = 0
    elif i == "緑" or 1:
        i = 1
    else:
        print("正しく入力してください。")
        continue
    if i == x:
        print("成功です。(一致)")
        count += 1
    else:
        print("失敗です。(不一致)\n最初に戻ります。")
        count = 0
    if count == 13:
        print("13回当てました。クリアです!")
        break