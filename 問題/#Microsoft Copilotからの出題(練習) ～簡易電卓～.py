# Microsoft Copilotからの出題(練習) ～簡易電卓～
def calculator(x):
    li = x.split()
    a, b, c = int(li[0]), li[1], int(li[2])
    match b:
        case "+":
            return a + c
        case "-":
            return a - c
        case "*":
            return a * c
        case "/":
            return a / c

print(calculator(input("計算式を入力してください(例:5 + 3)")))