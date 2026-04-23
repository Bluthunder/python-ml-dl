
from typing import List


def solve_n_queens(n: int)-> List[List[str]]:

    col = set()
    pos_diagonal = set()
    neg_diagonal = set()

    res = []
    board = [["."] * n for i in range(n)]


    def backtrack(r):
        if r == n:
            copy_board = [''.join(row) for row in board]
            res.append(copy_board)
            return


        for c in range(n):
            if c in col or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                continue

            col.add(c)
            pos_diagonal.add(r+c)
            neg_diagonal.add(r-c)

            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            pos_diagonal.remove(r+c)
            neg_diagonal.remove(r-c)
            board[r][c] = "."

    backtrack(0)
    return  res


if __name__ == '__main__':
    n = 4

    print(solve_n_queens(n))
