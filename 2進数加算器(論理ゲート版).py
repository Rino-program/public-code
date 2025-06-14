# 二進数計算機(論理ゲート)

def half(x, y):
    return (x & ~y) | (~x & y), x & y

def full(x, y, a):
    sum1, carry1 = half(x, y)
    sum2, carry2 = half(sum1, a)
    carry_out = carry1 | carry2
    return sum2, carry_out

def calculation(x, y):
    sum1, carry1 = half(x[4], y[4])
    sum2, carry2 = full(x[3], y[3], carry1)
    sum3, carry3 = full(x[2], y[2], carry2)
    sum4, carry4 = full(x[1], y[1], carry3)
    sum5, carry5 = full(x[0], y[0], carry4)
    return [sum1, sum2, sum3, sum4, sum5, carry5]

def main():
    print("二進数計算機(入力: 2進数 5bit以内, 出力: 2進数, 6bit以内)")
    x1 = input("2進数x : ")
    y1 = input("2進数y : ")
    x2 = [int(i) for i in x1.zfill(5)]
    y2 = [int(i) for i in y1.zfill(5)]
    result = calculation(x2, y2)
    result_str = "".join(map(str, result[::-1]))  # 逆順にして表示
    print("計算結果：{} + {} = {}".format(x1, y1, result_str))

if __name__ == "__main__":
    main()