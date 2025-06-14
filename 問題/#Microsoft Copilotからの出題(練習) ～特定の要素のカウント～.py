# Microsoft Copilotからの出題(練習) ～特定の要素のカウント～
def count_occurrences(lst, element):
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count

print(count_occurrences([1, 2, 2, 3, 4, 4, 5], 2))