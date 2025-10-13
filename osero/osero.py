# osero.py
"""
両者とも合法手が無い事がある。
"""
class osero:
    def __init__(self, size = 8):
        self.size = size
        # 駒を置けるかチェックする方向
        self.directions = [
            (-1, 0),  # 上
            (1, 0),   # 下
            (0, -1),  # 左
            (0, 1),   # 右
            (-1, -1), # 左上
            (-1, 1),  # 右上
            (1, -1),  # 左下
            (1, 1)    # 右下
        ]

        # Github Copilotのから提供 Thanks!
        """
        今後の予定
        強化学習に対応するために複数マップをすようできるようにする。
        案：
        initの引数で個数指定またはadd_board関数を作って実行
        動かすボードを引数で指定できるようにする
        """
        board_init = [[0 for _ in range(size)] for _ in range(size)]
        mid = size // 2
        # 初期配置
        board_init[mid-1][mid-1] = 1
        board_init[mid][mid] = 1
        board_init[mid-1][mid] = -1
        board_init[mid][mid-1] = -1
        self.board = board_init
        self.history = []
        self.turn = 0  # ←ここを 1 から 0 に修正

    def load_board_from_file(self, filename):
        board = []
        with open(filename, 'r') as file:
            for line in file:
                row = [int(cell) for cell in line.strip().split()]  # 空白を分割して整数に変換
                board.append(row)
        return board

    def print_board_human(self): # 人間用
        # "B" = -1 (黒), "W" = 1 (白), "." = 空き
        board = [['B' if cell == -1 else 'W' if cell == 1 else '.' for cell in row] for row in self.board]
        # 盤面の表示
        print("Othello Board(human):")
        print("Turn:", self.turn + 1)
        print("  c " + " ".join(map(str, list(range(self.size)))))
        print("r + " + "- " * len(board[0]) + "+")
        for i, row in enumerate(board):
            print(str(i) + " | " + " ".join(row) + " |")  # map(str, row) を削除
        print("  + " + "- " * len(board[0]) + "+")

    def print_board_human_can_place(self, piece): # 人間用
        # "B" = -1 (黒), "W" = 1 (白), "." = 空き
        board = [['B' if cell == -1 else 'W' if cell == 1 else '.' for cell in row] for row in self.board]
        # 盤面の表示
        print("Othello Board(human):")
        print("Turn:", self.turn + 1)
        print("  c " + " ".join(map(str, list(range(self.size)))))
        print("r + " + "- " * len(board[0]) + "+")
        for i, row in enumerate(board):
            row_str = " ".join(row)
            # 駒を置ける場所を示す
            for j in range(len(row)):
                if self.can_place_piece(i, j, piece):
                    row_str = row_str[:j*2] + '*' + row_str[j*2+1:]
            print(str(i) + " | " + row_str + " |")
        print("  + " + "- " * len(board[0]) + "+")

    def print_board_pc(self): # PC用
        print("Othello Board(PC):")
        for row in self.board:
            print(row)

    def can_place_piece(self, row, col, piece): # Github Copilotのから提供 Thanks! (自己改良済み)
        # 盤面のサイズ
        board = self.board
        rows = len(board)
        cols = len(board[0])

        # 駒の種類と相手の駒を定義
        opponent_piece = 1 if piece == -1 else -1

        # 座標が盤面外の場合、またはすでに駒が置かれている場合はFalse
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 0:
            return False

        # 8方向を確認
        for dr, dc in self.directions:
            r, c = row + dr, col + dc
            found_opponent = False

            # 相手の駒が続いているか確認
            while 0 <= r < rows and 0 <= c < cols and board[r][c] == opponent_piece:
                found_opponent = True
                r += dr
                c += dc

            # 相手の駒が続いた後に自分の駒があるか確認
            if found_opponent and 0 <= r < rows and 0 <= c < cols and board[r][c] == piece:
                return True

        # どの方向でも駒を置けない場合はFalse
        return False

    def line_change_piece(self, row, col, piece): # Github Copilotのから提供 Thanks! (自己改良済み)
        # 盤面のサイズ
        board = self.board
        rows = len(board)
        cols = len(board[0])

        # 各方向を確認して裏返す
        for dr, dc in self.directions:
            r, c = row + dr, col + dc
            path = []  # 挟んだ駒の座標を記録するリスト
            while 0 <= r < rows and 0 <= c < cols and board[r][c] != 0 and board[r][c] != piece:
                path.append((r, c))
                r += dr
                c += dc

            # 挟んだ駒がある場合、裏返す
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == piece:
                for pr, pc in path:
                    self.board[pr][pc] = piece
                    # 履歴に記録
                    self.history[-1]["row"].append(pr)
                    self.history[-1]["col"].append(pc)

    def add_piece(self, row, col, piece):
        board = self.board
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            raise ValueError("Row or column out of bounds")
        if self.can_place_piece(row, col, piece):
            board[row][col] = piece
            # ここで履歴を切り詰める
            if len(self.history) > self.turn:
                self.history = self.history[:self.turn]
            self.history.append({"row": [row], "col": [col], "piece": piece})
            self.turn += 1
            self.line_change_piece(row, col, piece)
        else:
            raise ValueError("Invalid move")

    def isnot_finished(self):
        # 盤面に空きがあるか確認
        for row in self.board:
            if 0 in row:
                return True
        return False

    def count_pieces(self):
        # どちらが多いか
        count = {1: 0, -1: 0, 0: 0}
        for row in self.board:
            for cell in row:
                if cell in count:
                    count[cell] += 1
        return count

    def piece_back(self):
        # 最後の手を戻す
        if self.turn <= 0:  # ←ここも0に修正
            raise ValueError("No moves to undo")
        print("piece_back")
        last_move = self.history[self.turn - 1]
        row, col = last_move["row"][0], last_move["col"][0]
        piece = last_move["piece"]
        self.board[row][col] = 0
        for i, j in zip(last_move["row"][1:], last_move["col"][1:]):
            self.board[i][j] = -piece
        self.turn -= 1
        return -piece  # 次に打つべき駒の色

    def piece_forward(self):
        # 最後の手を進める
        if self.turn >= len(self.history):
            raise ValueError("No moves to redo")
        print("piece_forward")
        last_move = self.history[self.turn]
        row, col = last_move["row"][0], last_move["col"][0]
        piece = last_move["piece"]
        self.board[row][col] = piece
        for i, j in zip(last_move["row"][1:], last_move["col"][1:]):
            self.board[i][j] = piece
        self.turn += 1
        return -piece  # 次に打つべき駒の色

    def piece_proposal(self, piece):
        # 駒を置ける場所を提案する
        proposals = []
        for r in range(self.size):
            for c in range(self.size):
                if self.can_place_piece(r, c, piece):
                    proposals.append((r, c))
        return proposals

def main():
    size = int(input("Enter board size (default 8): ") or 8)
    board = osero(size)
    board.print_board_pc()
    board.print_board_human()

    piece = int(input("Enter your piece (1 or -1): "))
    if piece not in [1, -1]:
        print("Invalid piece. Please enter 1 or -1.")
        return "Invalid piece start"

    while board.isnot_finished():
        print("Current board:")
        count = board.count_pieces()
        print(f"Count -> " + ", ".join(f"{i}: {v}" for i, v in count.items()) + ":")
        board.print_board_human_can_place(piece)
        print(f"Your piece: {piece}")
        if not board.piece_proposal(piece): # 駒を置ける場所がない場合
            print("No valid moves available.")
            piece = 1 if piece == -1 else -1  # Switch pieces
            board.turn += 1
            continue
        try:
            print("Enter coordinates using numbers, go back with 'b', go forward with 'e', and exit with minus sign.")
            col = input(f"Enter column (0-{board.size-1}): ")
            row = input(f"Enter row (0-{board.size-1}): ")
            com = [col, row]
            if "b" in com or "B" in com:
                piece = board.piece_back()
                continue
            elif "e" in com or "E" in com:
                piece = board.piece_forward()
                continue
            col, row = int(col), int(row)
            if col < 0 or row < 0:
                if input("Will you surrender?(y/n):") == "y":
                    count = board.count_pieces()
                    print(f"{-piece} Wins! / {piece} Loses...")
                    print(f"Count -> " + ", ".join(f"{i}: {v}" for i, v in count.items()) + ":")
                    board.print_board_human()
                    return "surrender break"
            board.add_piece(row, col, piece)
            piece = 1 if piece == -1 else -1  # Switch pieces
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
            return "Game interrupted"
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please contact the developer.")
    print("finish!\nFinal board:")
    count = board.count_pieces()
    print(f"Count -> " + ", ".join(f"{i}: {v}" for i, v in count.items()) + ":")
    print(f"{1 if count[1] > count[-1] else -1} Wins! / {1 if count[1] < count[-1] else -1} Loses...")
    board.print_board_human()
    input("Press Enter to exit...")
    return 0

if __name__ == "__main__":
    n = main()
    print("Exit code:", n)