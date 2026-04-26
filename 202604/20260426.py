# https://leetcode.com/problems/detect-cycles-in-2d-grid/

class Solution:
    """1559. Detect Cycles in 2D Grid

    Given a 2D array of characters grid of size m x n, you need to find if
    there exists any cycle consisting of the same value in grid.

    A cycle is a path of length 4 or more in the grid that starts and ends at
    the same cell. From a given cell, you can move to one of the cells adjacent
    to it - in one of the four directions (up, down, left, or right), if it has
    the same value of the current cell.

    Also, you cannot move to the cell that you visited in your last move. For
    example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from
    (1, 2) we visited (1, 1) which was the last visited cell.

    Return true if any cycle of the same value exists in grid, otherwise,
    return false.
    """
    def contains_cycle(self, grid: list[list[str]]) -> bool:
        if not grid or not grid[0]:
            return False
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i: int, j: int, pi: int, pj: int) -> bool:
            # Mark current cell as visited
            visited[i][j] = True
            for di, dj in directions:
                # Check all four adjacent cells
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j]:
                    if ni == pi and nj == pj:
                        # Skip the parent cell to avoid immediate backtrack
                        continue
                    if visited[ni][nj]:
                        # Back edge to visited cell (not parent) indicates cycle
                        return True
                    if dfs(ni, nj, i, j):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    # Start DFS from each unvisited cell with no parent
                    if dfs(i, j, -1, -1):
                        return True
        return False

    containsCycle = contains_cycle