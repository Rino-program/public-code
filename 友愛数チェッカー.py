def pn(num):
    num_keep, t = num, 0
    for _ in range(2):
        li = [1]
        for i in range(2, int(num**(1/2)) + 1):
            if num % i == 0:
                li.append(i)
                if i != num // i:
                    li.append(num // i)
        num = sum(li)
        if t == 0:
            num_keep2 = sum(li)
            t = 1
    return f"{num}と{num_keep2}は友愛数です。" if num_keep == num and num_keep != 1 and num != num_keep2 else f"{num_keep}は友愛数ではありません。"

print(pn(int(input("数を入力"))))