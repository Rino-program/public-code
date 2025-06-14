# Microsoft Copilotからの出題(練習) ～リストの重複を削除～
def remove_duplicates(lst):
    lsta = []
    for i in lst:
        if i not in lsta:
            lsta.append(i)
    return lsta
print(remove_duplicates(list(map(int, input("リストを入力(,で分割)").split(",")))))