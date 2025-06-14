def pn(num):
    lit = []
    for numr in range(num + 1):
        numr_keep = numr
        for j in range(2):
            li = [1]
            for i in range(2, int(numr**(1/2)) + 1):
                if numr % i == 0:
                    li.append(i)
                    if i != numr // i:
                        li.append(numr // i)
            numr = sum(li)
            if j == 0:
                num_keep2 = sum(li)
        if numr_keep == numr and numr != num_keep2 and numr < num_keep2:
            lit.append((numr, num_keep2))
    return lit

print(pn(int(input("回数"))))
