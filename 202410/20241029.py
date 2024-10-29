# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/


class Solution:
    """2684. Maximum Number of Moves in a Grid

    You are given a **0-indexed** `m x n` matrix `grid` consisting of **positive**
    integers.

    You can start at **any** cell in the first column of the matrix, and traverse the
    grid in the following way:

    * From a cell `(row, col)`, you can move to any of the cells: `(row - 1, col + 1)`,
    `(row, col + 1)` and `(row + 1, col + 1)` such that the value of the cell you move
    to, should be **strictly** bigger than the value of the current cell.

    Return *the **maximum** number of **moves** that you can perform.*

    """

    def max_moves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Initialize DP with 0 for first column
        dp = [[0 if j == 0 else -1 for j in range(n)] for _ in range(m)]

        moves = [(-1, 1), (0, 1), (1, 1)]

        for col in range(n - 1):
            for row in range(m):
                # If we can move from this cell
                if dp[row][col] != -1:
                    for dx, dy in moves:
                        new_row, new_col = row + dx, col + dy
                        if (
                            0 <= new_row < m
                            and new_col == col + 1
                            and grid[new_row][new_col] > grid[row][col]
                        ):
                            # Update only if the move is valid and increases our move count
                            dp[new_row][new_col] = max(
                                dp[new_row][new_col], dp[row][col] + 1
                            )

        # Find the maximum number of moves in the last column
        return max(max(row) for row in dp) if max(max(row) for row in dp) > 0 else 0

    maxMoves = max_moves
