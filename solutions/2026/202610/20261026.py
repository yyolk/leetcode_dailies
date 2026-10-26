# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/


class Solution:
    """3619. Count Islands With Total Value Divisible by K

    You are given an m x n matrix grid and a positive integer k. An island is
    a group of positive integers (representing land) that are 4-directionally
    connected (horizontally or vertically).

    The total value of an island is the sum of the values of all cells in the
    island.

    Return the number of islands with a total value divisible by k.

    Constraints:

    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 1000
    * 1 <= m * n <= 10**5
    * 0 <= grid[i][j] <= 10**6
    * 1 <= k <= 10**6
    """

    def count_islands(self, grid: list[list[int]], k: int) -> int:
        """Count islands whose cell sum is divisible by k.

        Args:
            grid (list[list[int]]): The grid of cell values.
            k (int): The positive divisor.

        Returns:
            int: Number of islands with total value divisible by k.
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    # Iterative DFS: sum positive cells and mark visited.
                    stack = [(r, c)]
                    island_sum = 0
                    while stack:
                        x, y = stack.pop()
                        if (
                            x < 0
                            or x >= rows
                            or y < 0
                            or y >= cols
                            or grid[x][y] <= 0
                        ):
                            continue
                        island_sum += grid[x][y]
                        grid[x][y] = 0  # mark visited
                        for dx, dy in directions:
                            stack.append((x + dx, y + dy))
                    if island_sum % k == 0:
                        count += 1
        return count

    countIslands = count_islands
