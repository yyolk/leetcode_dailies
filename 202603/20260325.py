# https://leetcode.com/problems/equal-sum-grid-partition-i

class Solution:
    """3546. Equal Sum Grid Partition I
    
    You are given an m x n matrix grid of positive integers. Your task is to
    determine if it is possible to make either one horizontal or one vertical
    cut on the grid such that each of the two resulting sections formed by the
    cut is non-empty. The sum of the elements in both sections is equal.
    Return true if such a partition exists; otherwise return false.
    """
    def can_partition_grid(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        # precompute row sums, column sums, and total sum in a single pass
        row_sums = [0] * m
        col_sums = [0] * n
        total_sum = 0
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                row_sums[i] += val
                col_sums[j] += val
                total_sum += val
        
        # if total is odd, equal partition is impossible
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        
        # check horizontal cuts: prefix of row sums equals target
        prefix = 0
        for i in range(m - 1):
            prefix += row_sums[i]
            if prefix == target:
                return True
        
        # check vertical cuts: prefix of column sums equals target
        prefix = 0
        for j in range(n - 1):
            prefix += col_sums[j]
            if prefix == target:
                return True
        
        return False

    canPartitionGrid = can_partition_grid