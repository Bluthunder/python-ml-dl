from typing import List

def surrounded_region(grid: List[List[str]])-> None:

    ROWS, COLS = len(board), len(board[0])

    # 1. Capture unsurrounded region ( O -> T)

    # 2. Capture surrounded_region (O -> X)

    # 3. Uncapture unsurrounded regions (T -> O)


    def capture(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O" :
            return

        board[r][c] = "T"

        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    # 1. Capture unsurrounded region ( O -> T)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):

                    capture(r, c)

    # 2. Capture surrounded_region (O -> X)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"

    # 3. Uncapture unsurrounded regions (T -> O)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "T":
                board[r][c] = "O"


if __name__ == '__main__':

    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

    print(surrounded_region(board))
