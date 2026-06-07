# https://leetcode.com/problems/maximum-number-of-points-with-cost/


class Solution:
    """1937. Maximum Number of Points with Cost

    You are given an `m x n` integer matrix `points` (**0\\-indexed**). Starting with `0`
    points, you want to **maximize** the number of points you can get from the matrix.

    To gain points, you must pick one cell in **each row**. Picking the cell at
    coordinates `(r, c)` will **add** `points[r][c]` to your score.

    However, you will lose points if you pick a cell too far from the cell that you
    picked in the previous row. For every two adjacent rows `r` and `r + 1` (where `0 <=
    r < m - 1`), picking cells at coordinates `(r, c1)` and `(r + 1, c2)` will
    **subtract** `abs(c1 - c2)` from your score.

    Return *the **maximum** number of points you can achieve*.

    `abs(x)` is defined as:

    * `x` for `x >= 0`.

    * `-x` for `x < 0`.

    """

    def max_points(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]  # Initialize the DP table with the first row

        for i in range(1, m):
            left_dp = [0] * n
            right_dp = [0] * n

            # Left-to-right sweep
            left_dp[0] = dp[0]
            for j in range(1, n):
                left_dp[j] = max(left_dp[j - 1] - 1, dp[j])

            # Right-to-left sweep
            right_dp[n - 1] = dp[n - 1]
            for j in range(n - 2, -1, -1):
                right_dp[j] = max(right_dp[j + 1] - 1, dp[j])

            # Update dp for the current row
            for j in range(n):
                dp[j] = points[i][j] + max(left_dp[j], right_dp[j])

        return max(dp)

    maxPoints = max_points
