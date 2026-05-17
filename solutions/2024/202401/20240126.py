# https://leetcode.com/problems/out-of-boundary-paths/
MOD = 10**9 + 7


class Solution:
    """576. Out of Boundary Paths

    There is an `m x n` grid with a ball. The ball is initially at the position
    `[start_row, start_column]`. You are allowed to move the ball to one of the four
    adjacent cells in the grid (possibly out of the grid crossing the grid boundary).
    You can apply **at most** `max_move` moves to the ball.

    Given the five integers `m`, `n`, `max_move`, `start_row`, `start_column`, return
    the number of paths to move the ball out of the grid boundary. Since the answer can
    be very large, return it **modulo** `109 + 7`.
    """

    def find_paths(
        self, m: int, n: int, max_move: int, start_row: int, start_column: int
    ) -> int:
        # Initialize DP array for counting paths
        dp = [[0] * n for _ in range(m)]
        # Start with the ball at the given position
        dp[start_row][start_column] = 1
        # Initialize count of paths
        count = 0

        # Iterate through each move
        for moves in range(1, max_move + 1):
            # Temporary DP array for updating counts
            temp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    # Check if the ball reaches the boundary in this move and update count
                    if i == m - 1:
                        count = (count + dp[i][j]) % MOD
                    if j == n - 1:
                        count = (count + dp[i][j]) % MOD
                    if i == 0:
                        count = (count + dp[i][j]) % MOD
                    if j == 0:
                        count = (count + dp[i][j]) % MOD

                    # Update the temporary DP array based on adjacent cells
                    temp[i][j] = (
                        (
                            (dp[i - 1][j] if i > 0 else 0)
                            + (dp[i + 1][j] if i < m - 1 else 0)
                        )
                        % MOD
                        + (
                            (dp[i][j - 1] if j > 0 else 0)
                            + (dp[i][j + 1] if j < n - 1 else 0)
                        )
                        % MOD
                    ) % MOD

            # Update the DP array for the next move
            dp = temp

        # Return the total count of paths reaching the boundary
        return count

    findPaths = find_paths
