"""
頭文字 ★4(400点)
writer: ウミツキ
"""

# code
a = """大きな石を
正しい位置に置くと
解ける。"""
a = a.split("\n")
for i in a:
    print(i[0])