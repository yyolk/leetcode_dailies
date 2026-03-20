# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix

from typing import List

class Solution:
    """3567. Minimum Absolute Difference in Sliding Submatrix
    
    For each k×k submatrix, return the min |a - b| for any two distinct values
    in that submatrix. If all values are equal, return 0.
    """
    def min_abs_diff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 1:
            # Single cell → no two distinct values → difference is 0
            return [[0] * len(grid[0]) for _ in range(len(grid))]

        m, n = len(grid), len(grid[0])
        rows = m - k + 1
        cols = n - k + 1

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # Collect all values in current k×k window
                vals = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.append(grid[r][c])

                # Sort to find min difference between any adjacent pair
                vals.sort()

                min_diff = float("inf")
                for p in range(1, len(vals)):
                    # Since sorted, adjacent differences are candidates
                    # min_diff must be between some pair of distinct values
                    if vals[p] != vals[p - 1]:
                        min_diff = min(min_diff, vals[p] - vals[p - 1])

                # If all equal, min_diff stays inf → set to 0
                ans[i][j] = 0 if min_diff == float("inf") else min_diff

        return ans

    minAbsDiff = min_abs_diff