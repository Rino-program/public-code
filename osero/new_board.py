import sys

def create_othello_board(size=8): # Github Copilotのから提供 Thanks!
    board = [[0 for _ in range(size)] for _ in range(size)]
    mid = size // 2
    # 初期配置
    board[mid-1][mid-1] = 1
    board[mid][mid] = 1
    board[mid-1][mid] = -1
    board[mid][mid-1] = -1
    return board

def save_board(board, filename):
    with open(filename, 'w') as f:
        for row in board:
            f.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    board = create_othello_board(size)
    save_board(board, "othello_initial_board.txt")