# https://leetcode.com/problems/minimum-xor-path-in-a-grid/


class Solution:
    """3882. Minimum XOR Path in a Grid

    You are given a 2D integer array grid of size m * n.

    You start at the top-left cell (0, 0) and want to reach the bottom-right
    cell (m - 1, n - 1).

    At each step, you may move either right or down.

    The cost of a path is defined as the bitwise XOR of all the values in the
    cells along that path, including the start and end cells.

    Return the minimum possible XOR value among all valid paths from (0, 0) to
    (m - 1, n - 1).

    Constraints:

    * 1 <= m == grid.length <= 1000

    * 1 <= n == grid[i].length <= 1000

    * m * n <= 1000

    * 0 <= grid[i][j] <= 1023
    """

    def min_cost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Track all possible XOR values reachable at each cell.
        # Values are in [0, 1023], so at most 1024 distinct XORs per cell.
        reachable: list[list[set[int]]] = [[set() for _ in range(n)] for _ in range(m)]
        reachable[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                # Skip the starting cell which is already initialized.
                if i == 0 and j == 0:
                    continue
                # Collect XORs from the left cell (if exists).
                if j > 0:
                    for prev in reachable[i][j - 1]:
                        reachable[i][j].add(prev ^ grid[i][j])
                # Collect XORs from the upper cell (if exists).
                if i > 0:
                    for prev in reachable[i - 1][j]:
                        reachable[i][j].add(prev ^ grid[i][j])

        # The answer is the smallest XOR that can reach the bottom-right cell.
        return min(reachable[m - 1][n - 1])

    minCost = min_cost
