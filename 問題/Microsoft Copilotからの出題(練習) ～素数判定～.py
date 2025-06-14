# Microsoft Copilotからの出題(練習) ～素数判定～
def pnf(x):
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3, int(x**(1/2)) + 1, 2):
        if x % i == 0:
            return False
    return True

print(pnf(int(input("数字を入力"))))