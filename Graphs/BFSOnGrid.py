
from typing import List
from collections import deque

def bfs(grid: List[List[int]], start_row: int, start_col: int)->None:

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    queue = deque()

    queue.append((start_row, start_col))

    visited[start_row][start_col] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    while queue:
        row, col = deque.popleft()

        for dr, dc in directions:
            if 0<=(row+dr)<rows and
               0<=(col+dc)<cols and
               not visited[row+dr][col+dc]:
                   visited[row+dr][col+dc]=True
                   queue.append((row+dr, col+dc))




    
