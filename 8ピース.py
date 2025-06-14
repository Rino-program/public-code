from copy import deepcopy as dc

#puzzleに最初の状態を入れてください。
#goalには目標とする状態を入れてください。
puzzle = [
    [2, 0, 4],
    [3, 5, 8],
    [1, 6, 7]
]
queue = [puzzle]
next_queue = []
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
visited = {tuple(map(tuple, puzzle)): None} # 初期状態をタプルに変換して訪問済みリストに追加
operable = []
x, y = 0, 0

# 検査
check = 0
for i in range(9):
    for j in puzzle:
        if i in j:
            check += 1
if check != 9:
    print("リストが正しくありません。")

# 候補作成
def explored(li):
    # 0の場所を探す。
    index_num = (0, 0)
    num = 0
    for i in li:
        if 0 in i:
            index_num = (num, i.index(0))
        num += 1
    # 操作をリストアップ
    operable = []
    y, x = index_num
    if x < 2:
        operable.append(1) # 右
    if x > 0:
        operable.append(3) # 左
    if y > 0:
        operable.append(0) # 上
    if y < 2:
        operable.append(2) # 下
    return operable, index_num

found = False # 目標状態に到達したかどうかのフラグ

while queue:
    current_state = queue.pop(0)
    if tuple(map(tuple, current_state)) == tuple(map(tuple, goal)):
        found = True
        break
    operable, index_num = explored(current_state)
    y, x = index_num
    for move in operable:
        new_puzzle = dc(current_state) # パズルをコピー（ディープコピー）
        if move == 0: # 上に移動
            new_puzzle[y][x], new_puzzle[y-1][x] = new_puzzle[y-1][x], new_puzzle[y][x]
        elif move == 1: # 右に移動
            new_puzzle[y][x], new_puzzle[y][x+1] = new_puzzle[y][x+1], new_puzzle[y][x]
        elif move == 2: # 下に移動
            new_puzzle[y][x], new_puzzle[y+1][x] = new_puzzle[y+1][x], new_puzzle[y][x]
        elif move == 3: # 左に移動
            new_puzzle[y][x], new_puzzle[y][x-1] = new_puzzle[y][x-1], new_puzzle[y][x]
        new_puzzle_tuple = tuple(map(tuple, new_puzzle))
        if new_puzzle_tuple not in visited:
            next_queue.append(new_puzzle)
            visited[new_puzzle_tuple] = (tuple(map(tuple, current_state)), move) # new_puzzleをタプルに変換して追加
    queue.extend(next_queue)
    next_queue = []

if found:
    print("目標状態に到達しました。")
    # 操作手順を逆順にたどって出力
    steps = []
    state = tuple(map(tuple, goal))
    while state:
        if visited[state] == None:
            break
        prev_state, move = visited[state]
        steps.append(move)
        state = prev_state
    steps.reverse()
    print("操作手順:", steps)
else:
    print("目標状態に到達できませんでした。")
