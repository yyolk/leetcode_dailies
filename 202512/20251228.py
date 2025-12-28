# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix


class Solution:
    """1351. Count Negative Numbers in a Sorted Matrix

    Given a m x n matrix grid sorted in non-increasing order both row-wise
    and column-wise, return the number of negative numbers in grid.
    """
    def countNegatives(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Start from bottom-left corner: negatives are to the right
        row = m - 1
        col = 0
        
        while row >= 0 and col < n:
            # If current element is negative, entire segment to the right is negative
            if grid[row][col] < 0:
                count += n - col               # All columns from col to n-1 are negative
                row -= 1                       # Move up to previous row
            else:
                # Current element non-negative, move right to find negatives
                col += 1
        
        return count

    countNegatives = countNegatives