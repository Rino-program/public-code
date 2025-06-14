# Microsoft Copilotからの出題(練習) ～回文チェック～
def pc(text):
    return text == str(text)[::-1]

print(pc(input("回文チェッカー。文字列を入力して下さい。")))