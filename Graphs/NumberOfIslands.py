from typing import List

def numIslands(grid: List[List[str]]) -> int:
    if grid == None or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid,i,j)
                count += 1
    return count

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return -1

    grid[i][j] = '0'

    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i ,j + 1)
    dfs(grid, i, j - 1)




def numIslands(grid: List[List[str]])-> int:

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == '1' and
                    (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands


if __name__ == '__main__':
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]

    print(numIslands(grid))
