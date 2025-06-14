#Microsoft Copilotからの出題(練習) ～数独処理～
x=[
    [0, 3, 0, 0, 8, 0, 0, 0, 0],
    [7, 4, 0, 0, 0, 1, 2 ,8, 0],
    [2, 0, 8, 0, 4, 9, 3, 0, 6],
    [0, 0, 3, 8, 0, 0, 0, 6, 2],
    [0, 9, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 1, 0, 0, 3, 0, 4, 8],
    [0, 8, 0, 1, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 2, 0, 0, 9, 0],
    [4, 0, 0, 7, 3, 5, 0, 2, 0]
]

# チェック
def check(a, b, li, k):
    for i in range(9):
        if li[a][i] == k or li[i][b] == k:
            return False
    start_a, start_b = 3 * (a // 3), 3 * (b // 3)
    for i in range(start_a, start_a + 3):
        for j in range(start_b, start_b + 3):
            if li[i][j] == k:
                return False
    return True

# 計算
def f(li):
    for a in range(9):
        for b in range(9):
            if li[a][b] == 0:
                for k in range(1, 10):
                    if check(a, b, li, k):
                        li[a][b] = k
                        if f(li):
                            return True
                        li[a][b] = 0
                return False
    return True

# 表示
if f(x):
    for row in x:
        print(row)
else:
    print("No solution exists")
