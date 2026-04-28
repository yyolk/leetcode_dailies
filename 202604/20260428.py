# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

class Solution:
    """2033. Minimum Operations to Make a Uni-Value Grid
    
    You are given a 2D integer grid of size m x n and an integer x. In one
    operation, you can add x to or subtract x from any element in the grid.
    A uni-value grid is a grid where all the elements of it are equal.
    Return the minimum number of operations to make the grid uni-value. If it
    is not possible, return -1.
    """
    def min_operations(self, grid: list[list[int]], x: int) -> int:
        # Flatten grid into list of all values for easier processing
        vals = [num for row in grid for num in row]
        if not vals:
            return 0
        # All elements must have identical remainder when divided by x
        # otherwise, cannot reach same value
        r = vals[0] % x
        for v in vals:
            if v % x != r:
                return -1
        # Sorting allows direct access to median which minimizes
        # the sum of absolute deviations
        vals.sort()
        n = len(vals)
        median = vals[n // 2]
        # Total operations: sum of |val - median| // x for all vals
        # Division is exact due to same modulo
        return sum(abs(v - median) // x for v in vals)

    minOperations = min_operations