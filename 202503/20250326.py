# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/


class Solution:
    """2033. Minimum Operations to Make a Uni-Value Grid

    You are given a 2D integer `grid` of size `m x n` and an integer `x`. In one
    operation, you can **add** `x` to or **subtract** `x` from any element in the
    `grid`.

    A **uni-value grid** is a grid where all the elements of it are equal.

    Return *the **minimum** number of operations to make the grid **uni-value***. If it
    is not possible, return `-1`."""

    def min_operations(self, grid: list[list[int]], x: int) -> int:
        # Get dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Compute the remainder of the first element modulo x
        r = grid[0][0] % x
        
        # List to store transformed values
        b_list = []
        
        # Check if all elements have the same remainder modulo x
        # and compute transformed values
        for i in range(m):
            for j in range(n):
                a = grid[i][j]
                if a % x != r:
                    return -1  # Impossible if remainders differ
                b = (a - r) // x
                b_list.append(b)
        
        # Sort the list to find the median
        b_list.sort()
        
        # Find the median (for both odd and even lengths, this works)
        median = b_list[len(b_list) // 2]
        
        # Calculate total operations as sum of absolute differences from median
        total_operations = sum(abs(b - median) for b in b_list)
        
        return total_operations

    minOperations = min_operations
