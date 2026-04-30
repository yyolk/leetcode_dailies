# https://leetcode.com/problems/maximum-path-score-in-a-grid/

class Solution:
    """3742. Maximum Path Score in a Grid

    You are given an m x n grid where each cell contains one of the values 0, 1,
    or 2. You are also given an integer k. You start from the top-left corner
    (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving
    only right or down. Each cell contributes a specific score and incurs an
    associated cost, according to their cell values: 0: adds 0 to your score and
    costs 0. 1: adds 1 to your score and costs 1. 2: adds 2 to your score and
    costs 1. Return the maximum score achievable without exceeding a total cost
    of k, or -1 if no valid path exists. Note: If you reach the last cell but
    the total cost exceeds k, the path is invalid.
    """
    def max_path_score(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return -1

        # prev_dp[j][used]: max score reaching (prev_row, j) with exact cost 'used'
        prev_dp = [[-1] * (k + 1) for _ in range(n)]

        # starting cell
        start_cell = grid[0][0]
        start_score = start_cell
        start_cost = 0 if start_cell == 0 else 1
        if start_cost <= k:
            prev_dp[0][start_cost] = start_score

        # fill first row (only from left)
        for j in range(1, n):
            cell = grid[0][j]
            cell_score = cell
            cell_cost = 0 if cell == 0 else 1
            for used in range(k + 1):
                prev_used = used - cell_cost
                if prev_used >= 0 and prev_dp[j - 1][prev_used] != -1:
                    prev_dp[j][used] = max(
                        prev_dp[j][used], prev_dp[j - 1][prev_used] + cell_score
                    )

        # fill remaining rows
        for i in range(1, m):
            # new row dp
            curr_dp = [[-1] * (k + 1) for _ in range(n)]

            # first column of this row (only from above)
            cell = grid[i][0]
            cell_score = cell
            cell_cost = 0 if cell == 0 else 1
            for used in range(k + 1):
                prev_used = used - cell_cost
                if prev_used >= 0 and prev_dp[0][prev_used] != -1:
                    curr_dp[0][used] = max(
                        curr_dp[0][used], prev_dp[0][prev_used] + cell_score
                    )

            # rest of the row (from left and above)
            for j in range(1, n):
                cell = grid[i][j]
                cell_score = cell
                cell_cost = 0 if cell == 0 else 1
                for used in range(k + 1):
                    prev_used = used - cell_cost
                    if prev_used >= 0:
                        # from above
                        if prev_dp[j][prev_used] != -1:
                            curr_dp[j][used] = max(
                                curr_dp[j][used],
                                prev_dp[j][prev_used] + cell_score
                            )
                        # from left
                        if curr_dp[j - 1][prev_used] != -1:
                            curr_dp[j][used] = max(
                                curr_dp[j][used],
                                curr_dp[j - 1][prev_used] + cell_score
                            )

            prev_dp = curr_dp

        # find max score at bottom-right with any cost <= k
        ans = -1
        for used in range(k + 1):
            if prev_dp[n - 1][used] != -1:
                ans = max(ans, prev_dp[n - 1][used])
        return ans

    maxPathScore = max_path_score