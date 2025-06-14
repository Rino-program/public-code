# Microsoft Copilotからの出題(練習) ～数値の合計と平均～
def nta2(x):
    return {"合計": sum(x), "平均": sum(x) / len(x)}

print(nta2(list(map(int, input("リストを入力").split(",")))))