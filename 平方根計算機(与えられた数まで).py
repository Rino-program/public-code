def test(num):
    li = []
    for i in range(1, num + 1):
        li.append((i, i**0.5))
    return li

print(test(int(input("数字を入力"))))
