# https://leetcode.com/problems/maximum-score-from-grid-operations/

class Solution:
    """3225. Maximum Score From Grid Operations
    
    You are given a 2D matrix grid of size n x n. Initially, all cells of the grid
    are colored white. In one operation, you can select any cell of indices (i, j),
    and color black all the cells of the jth column starting from the top row down
    to the ith row. The grid score is the sum of all grid[i][j] such that cell
    (i, j) is white and it has a horizontally adjacent black cell. Return the
    maximum score that can be achieved after some number of operations.
    """
    def maximum_score(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # prefix[j][i] := sum of first i elements (rows 0..i-1) in column j
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]
        # prev_pick[i]: max score up to prev col, with h[prev_col] = i
        # (i black cells from top)
        prev_pick = [0] * (n + 1)
        # prev_skip[i]: max score up to prev col, tracking prev-prev for skip
        prev_skip = [0] * (n + 1)
        for j in range(1, n):
            curr_pick = [0] * (n + 1)
            curr_skip = [0] * (n + 1)
            for curr in range(n + 1):
                for prev in range(n + 1):
                    if curr > prev:
                        # curr deeper: add white cells from prev..curr in j-1
                        # that touch the deeper curr black in j
                        score = prefix[j - 1][curr] - prefix[j - 1][prev]
                        curr_pick[curr] = max(curr_pick[curr], prev_skip[prev] + score)
                        curr_skip[curr] = max(curr_skip[curr], prev_skip[prev] + score)
                    else:
                        # prev deeper: add white cells from curr..prev in j
                        # that touch prev black in j-1 (for pick)
                        score = prefix[j][prev] - prefix[j][curr]
                        curr_pick[curr] = max(curr_pick[curr], prev_pick[prev] + score)
                        curr_skip[curr] = max(curr_skip[curr], prev_pick[prev])
            prev_pick = curr_pick
            prev_skip = curr_skip
        return max(prev_pick)

    maximumScore = maximum_score