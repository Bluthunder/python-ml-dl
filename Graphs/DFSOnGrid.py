from typing import List

def dfs_recursive(grid: List[List[int]], row :int, col: int, visited: List[List[bool]])-> None:

    rows = len(grid)
    cols = len(grid[0])

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return


    if visited[row][col]:
        return

    visited[row][col] = True
    print(grid[row][col])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr , dc in directions:
        dfs_recursive(grid, row+dr, col+dc, visited)



def dfs_iterative(grid: List[List[int]], row:int, col: int)->None:

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    stack = []

    stack.append((row, col))

    directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

    while stack:
        row, col = stack.pop()

        if row < 0 or row >= rows or col < 0  or col >= cols:
            continue

        if visited[row][col]:
            continue

        visited[row][col] = True

        print(f'Visiting --> {grid[row][col]} at {row}, {col}')

        for dc, dr in directions:
            stack.append((row+dr, col+dc))



if __name__ == '__main__':

    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    dfs_recursive(grid=grid, row=0, col=0, visited=visited)


    print('--*************--')

    dfs_iterative(grid=grid, row=0, col=0)
