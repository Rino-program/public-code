# Microsoft Copilotからの出題(練習) ～フィボナッチ数列～
def fs(x):
    a, b = 0, 1
    li = []
    for i in range(x):
        li.append(a)
        a, b = b, a + b
    return li

print(fs(int(input("出力する要素数を入力"))))