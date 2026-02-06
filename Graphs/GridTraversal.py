
from typing import List


def linear_traversal(grid: List[List[int]]) -> None:

    print(f'Linear Traversal')

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            print(f'Linear Traversal --> {grid[r][c]}')



def diagonal_traversal(grid: List[List[int]]) -> None:
    print(f'Diagonal Traversal')

    r = len(grid)
    c = len(grid[0])

    for d in range(r+c-1):
        nr = max(0, d-c+1)
        nc = max(0, c-1-d)

        while nr < r and nc < c:
            print(f'Diagonal Element --> {grid[nr][nc]}')
            nr += 1
            nc += 1


def spiral_traversal(grid:List[List[int]]) -> None:
    results = []

    rows = len(grid)
    cols = len(grid[0])

    if len(grid) == 0:
        return results

    top , bottom = 0 , rows - 1
    left , right = 0, cols - 1

    while (top <= bottom and left <= right):

        # Move Right
        for c in range(left, right+1):
            results.append(grid[top][c])

        top += 1

        # Move down
        for r in range(top, bottom+1):
            results.append(grid[r][right])

        right -= 1

        # Move left
        if top <= bottom:
            for c in range(right, left-1, -1):
                results.append(grid[bottom][c])
            bottom -= 1

         # Move up
        if left <= right:
            for r in range(bottom, top - 1, -1):
                results.append(grid[r][left])
            left += 1
    return results


if __name__ == '__main__':
    grid = [
        [1, 2, 3],
        [5, 6, 7],
        [8, 9, 10]
    ]

    diagonal_traversal(grid)
    print('/n')
    print('*****************')
    print('/n')
    linear_traversal(grid)
    print('/n')
    print('*****************')
    print('/n')
    print(spiral_traversal(grid))
