def li(x):
    if len(x) < 2:
        return x
    for i in range(len(x)):
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x.insert(i, x.pop(i + 1))
    return x[-1]

print(li(list(map(int, input("リストを入力してください。").split(",")))))