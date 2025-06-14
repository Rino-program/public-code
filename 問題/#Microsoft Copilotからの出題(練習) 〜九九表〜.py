#九九表の生成: 1から9までの数字を使って九九表を出力するプログラムを作成してください
for i in range(1,15):
    for j in range(1,15):
        print(i*j,end = " ")
    print()