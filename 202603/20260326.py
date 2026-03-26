# https://leetcode.com/problems/equal-sum-grid-partition-ii

class Solution:
    """3548. Equal Sum Grid Partition II
    
    You are given an m x n matrix grid of positive integers. Your task is to
    determine if it is possible to make either one horizontal or one vertical cut
    on the grid such that each of the two resulting sections formed by the cut is
    non-empty. The sum of elements in both sections is equal, or can be made equal
    by discounting at most one single cell in total (from either section). If a
    cell is discounted, the rest of the section must remain connected. Return true
    if such a partition exists; otherwise, return false. Note: A section is
    connected if every cell in it can be reached from any other cell by moving up,
    down, left, or right through other cells in the section.
    """
    def can_partition_grid(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        if m * n < 2:
            return False
        MAX_V = 10**5
        # precompute min/max row and col indices per value for O(1) existence
        # checks in any row/col range (used only for thick sections)
        min_r = [m] * (MAX_V + 1)
        max_r = [-1] * (MAX_V + 1)
        min_c = [n] * (MAX_V + 1)
        max_c = [-1] * (MAX_V + 1)
        S = 0
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                S += v
                min_r[v] = min(min_r[v], i)
                max_r[v] = max(max_r[v], i)
                min_c[v] = min(min_c[v], j)
                max_c[v] = max(max_c[v], j)
        # horizontal cuts: O(m) after O(mn) precompute
        if m >= 2:
            row_prefix = [0] * (m + 1)
            for i in range(m):
                row_sum = sum(grid[i])
                row_prefix[i + 1] = row_prefix[i] + row_sum
            for r in range(m - 1):
                sum_top = row_prefix[r + 1]
                sum_bot = S - sum_top
                if sum_top == sum_bot:
                    return True
                diff = abs(sum_top - sum_bot)
                if diff > MAX_V or diff == 0:
                    continue
                # determine larger side and its row bounds
                if sum_top > sum_bot:
                    h_sec = r + 1
                    start_row = 0
                    end_row = r
                    is_top = True
                else:
                    h_sec = m - r - 1
                    start_row = r + 1
                    end_row = m - 1
                    is_top = False
                # thick (>=2 rows and >=2 cols): any cell can be removed
                if n >= 2 and h_sec >= 2:
                    if is_top:
                        if min_r[diff] <= end_row:
                            return True
                    else:
                        if max_r[diff] >= start_row:
                            return True
                else:
                    # thin line: only endpoint cells allowed; skip 1x1
                    if h_sec * n == 1:
                        continue
                    if h_sec == 1:
                        # single-row strip: check leftmost/rightmost
                        rowi = start_row
                        if grid[rowi][0] == diff or grid[rowi][n - 1] == diff:
                            return True
                    else:
                        # single-col strip: check topmost/bottommost
                        if grid[start_row][0] == diff or grid[end_row][0] == diff:
                            return True
        # vertical cuts: symmetric to horizontal
        if n >= 2:
            col_prefix = [0] * (n + 1)
            for j in range(n):
                col_sum = sum(grid[i][j] for i in range(m))
                col_prefix[j + 1] = col_prefix[j] + col_sum
            for c in range(n - 1):
                sum_left = col_prefix[c + 1]
                sum_right = S - sum_left
                if sum_left == sum_right:
                    return True
                diff = abs(sum_left - sum_right)
                if diff > MAX_V or diff == 0:
                    continue
                if sum_left > sum_right:
                    w_sec = c + 1
                    start_col = 0
                    end_col = c
                    is_left = True
                else:
                    w_sec = n - c - 1
                    start_col = c + 1
                    end_col = n - 1
                    is_left = False
                if m >= 2 and w_sec >= 2:
                    if is_left:
                        if min_c[diff] <= end_col:
                            return True
                    else:
                        if max_c[diff] >= start_col:
                            return True
                else:
                    if m * w_sec == 1:
                        continue
                    if w_sec == 1:
                        # single-col strip: check top/bottom
                        colj = start_col
                        if grid[0][colj] == diff or grid[m - 1][colj] == diff:
                            return True
                    else:
                        # single-row strip: check leftmost/rightmost
                        rowi = 0
                        if grid[rowi][start_col] == diff or grid[rowi][end_col] == diff:
                            return True
        return False

    canPartitionGrid = can_partition_grid