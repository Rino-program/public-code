import time # 実行速度測定用
q = int(input())
li_n = []
li_s = []
kekka = []
for _ in range(q):
    if (ln := len(li := list(map(int, input().split())))) == 3:
        li_n.append(li[1])
        li_s.append(li[2])
        continue
    if ln == 2:
        start = time.time()
        s = 0
        n = li[1]
        while n != 0:
            a = li_n[0]
            b = li_s[0]
            d = a - n
            if d > 0:
                s += b * n
                li_n[0] -= n
                n = 0
            elif d == 0:
                s += b * n
                del li_n[0], li_s[0]
                n = 0
            else:
                s += b * a
                del li_n[0], li_s[0]
                n = -d
        kekka.append(s)
        end = time.time()
        print(f"実行時間: {end - start}秒")

print(*kekka, sep='\n')
