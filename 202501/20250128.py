# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/


class Solution:
    """2658. Maximum Number of Fish in a Grid

    You are given a **0-indexed** 2D matrix `grid` of size `m x n`, where `(r, c)`
    represents:

    * A **land** cell if `grid[r][c] = 0`, or

    * A **water** cell containing `grid[r][c]` fish, if `grid[r][c] > 0`.

    A fisher can start at any **water** cell `(r, c)` and can do the following
    operations any number of times:

    * Catch all the fish at cell `(r, c)`, or

    * Move to any adjacent **water** cell.

    Return *the **maximum** number of fish the fisher can catch if he chooses his
    starting cell optimally, or* `0` if no water cell exists.

    An **adjacent** cell of the cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c
    - 1)`, `(r + 1, c)` or `(r - 1, c)` if it exists."""

    def find_max_fish(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        max_fish = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] == 0:
                return 0

            visited[r][c] = True
            fish_count = grid[r][c]

            # Check all four directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                fish_count += dfs(r + dr, c + dc)

            return fish_count

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:  # Check if not visited
                    fish = dfs(i, j)
                    max_fish = max(max_fish, fish)

        # Clear visited array for the next iteration if needed
        for i in range(m):
            for j in range(n):
                visited[i][j] = False

        return max_fish

    findMaxFish = find_max_fish
