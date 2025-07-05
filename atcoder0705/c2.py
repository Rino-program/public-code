q = int(input())
li_n = []
li_s = []
kekka = []
kyo = [] # 距離
g = 0
goukei = [] # 合計
kyo_s = 0
z = 0 # 前回のずれを反映するための変数
for _ in range(q):
    if (ln := len(li := list(map(int, input().split())))) == 3:
        li_n.append(li[1])
        li_s.append(li[2])
        kyo.append(li[1] + kyo_s)
        kyo_s += li[1]
        g += li[2] * li[1]
        goukei.append(g)
        continue
    if ln == 2:
        # 前回のずれを反映
        l = z
        r = len(kyo)
        s = 0
        n = li[1]
        while l == r - 1:
            # 二分探索
            if goukei[l] <= n < goukei[r - 1]:
                r = (l + r) // 2
            else:
                l = (l + r) // 2
        s += goukei[l]
        n -= kyo[l]
        if n == 0:
            kekka.append(s)
            continue
        s += n * li_s[r - 1]
        z = n + kyo[l] - kyo[r - 1]
        kekka.append(s)

print(*kekka, sep='\n')
