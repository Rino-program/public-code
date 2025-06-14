"""
柴犬列 500
writer: まちょ

まちょ君は柴犬が大好きです。そこでまちょ君は、文字列にも柴犬を見つけ出そうとしました。
まちょ君は、ある文字列に 's', 'b', 'i' ,'n' がこの順で含まれるとき、その文字列を「柴犬列」であるとしました。
まちょ君は小さな柴犬が好きなので、できるだけ長さの小さい柴犬列を見つけたいです。

文字列Sが与えられるので、その連続した部分文字列のうち柴犬列となるものの最小の長さを求めてください。またそのような柴犬列を見つけられなかったときは"No"と出力してください。

制約
1<=len(S)<=100 ,Sは小文字のアルファベットのみで構成される。

必要な変数
S str型

入力例1
S = "iloveshibainu"
出力例1
7

～入力例と出力例集～
1	
S = "iloveshibainu"
7

2	
S = "gwsibrhnijihlxzbhjnvbwqiybvgyivtsxbcwrn"
17

3	
S = "cybxqkdbnastsmkbjsysjtozzzqmulzrnejybqibfvdxajwevfmijnsyuuuztyjsrsrfmsqqxsru"
35

4	
S = "mmjgtipoutenkgqynusjfntnssfosehnnxgabtnzmwqoidqplcupfighiaknarboyaehdwaqdkbaxuuvqa"
32

5	
S = "u"
No

6	
S = "swplbfxxrenwkbeceyonc"
No

7	
S = "ubznduwiybbwcpzolgfivyzvnqqvnqsvogtsqxbpmkbrr"
No

8	
S = "wsrrlcdjkhvcxjgajfswzdbydmkgctpostazihujpingadjqgnicmfcntmogrxo"
25

9	
S = "qwdyagxmvmbshvzhxswnziarcnfybvifpkqqkmspkiyptvbzajklxyvienkbgdeqoingkklvnymvb"
20

10	
S = "likmpevsedkasb"
No

11	
S = "xzpptvboizlbeiiwunhtbszohvxkbslnzpkvncxoddirqbkuijnnidpnfsshinnpnbbtu"
22
"""
"""
#再帰のexample
def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)  # なんだか不思議な感じ..
"""
# code
S = "xzpptvboizlbeiiwunhtbszohvxkbslnzpkvncxoddirqbkuijnnidpnfsshinnpnbbtu"

n = len(S)
m = 101 #このプログラム内では101が未発見を表す値とする。

def sbin_find(S, i, n): # 指定された's'から始まる最短の's'->'b'->'i'->'n'を1組探す。
    length = 1
    step = 0
    while i < n:
        length += 1
        if step == 0 and S[i] == "b":
            step += 1
        elif step == 1 and S[i] == "i":
            step += 1
        elif step == 2 and S[i] == "n":
            return length
        i += 1
    return 101

for i in range(n): #Sの中で's'の場所を探す。
    if S[i] == "s":
        m = min(m, sbin_find(S, i+1, n))
if m == 101:
    print("No")
else:
    print(m)