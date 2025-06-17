# coding: utf-8
# Your code here!

def tngrs(numa, numb, numc):
    def hei(a):
        a = str(a)
        if a[0] == "√":
            return int(a[1:])
        else:
            try:
                return int(a) ** 2
            except:
                if "√" in a:
                    nums =a.split("√")
                    if all(part.isdigit() for part in nums):
                        return (int(nums[1]) * (int(nums[0]) ** 2))
    x_index, cr = 0, 0
    if not numa or numa == "0":
        x_index += 3
    else:
        numa = hei(numa)
        if isinstance(numa, str):
            return numa
    if not numb or numb == "0":
        x_index += 4
    else:
        numb = hei(numb)
        if isinstance(numb, str):
            return numb
    if not numc or numc == "0":
        x_index += 5
    else:
        numc = hei(numc)
        if isinstance(numc, str):
            return numc
    if x_index > 6 or x_index < 3:
        return "エラー：引数の数が正しくありません。"
    try:
        if x_index == 3:
            cr = numc - numb
        elif x_index == 4:
            cr = numc - numa
        elif x_index == 5:
            cr = numa + numb
    except:
        return "エラー：計算できません。"
    try:
        if cr ** (1 / 2) == int(cr ** (1 / 2)):
            return cr ** (1 / 2)
        else:
            def ease_root(n):
                i = 2
                a = 1
                while (i ** 2) <= n:
                    if n % (i ** 2) == 0:
                        n //= (i ** 2)
                        a *= i
                    else:
                        i += 1
                if n == 1:
                    return a
                elif a == 1:
                    return f"√{n}"
                else:
                    return f"{a}√{n}"
        return ease_root(cr)
    except:
        return "エラー：直角三角形が存在しない可能性があります。"
print("a^2 + b^2 = c^2 の a,b,c を入力してください。\n求めたい文字には入力しないか、0を入力してください。")
an, bn, cn = input("aを入力"), input("bを入力"), input("cを入力")
print(tngrs(an, bn, cn))
