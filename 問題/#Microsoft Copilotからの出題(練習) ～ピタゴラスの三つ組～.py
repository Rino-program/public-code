# Microsoft Copilotからの出題(練習) ピタゴラスの三つ組
def fpt(num):
    li = []
    for i in range(1, num):
        for j in range(i, num):
            for k in range(j, num):
                if i**2 + j**2 == k**2:
                    li.append((i, j, k))
    return li

print(fpt(int(input("数を入力"))))
