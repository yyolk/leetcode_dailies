# https://leetcode.com/problems/find-missing-and-repeated-values/


class Solution:
    """2965. Find Missing and Repeated Values

    You are given a **0-indexed** 2D integer matrix `grid` of size `n * n` with values
    in the range `[1, n2]`. Each integer appears **exactly once** except `a` which
    appears **twice** and `b` which is **missing**. The task is to find the repeating
    and missing numbers `a` and `b`.

    Return *a **0-indexed** integer array* `ans` *of size* `2` *where* `ans[0]` *equals
    to* `a` *and* `ans[1]` *equals to* `b`*.*"""

    def find_missing_and_repeated_values(self, grid: list[list[int]]) -> list[int]:
        # Get the size n of the grid (n x n)
        n = len(grid)
        
        # Create a count array to track frequency of each number
        # Size is n*n + 1 because numbers range from 1 to n²
        count = [0] * (n * n + 1)
        
        # Count occurrences of each number in the grid
        for row in grid:
            for num in row:
                count[num] += 1
        
        # Variables to store our answers
        repeated = None
        missing = None
        
        # Find the repeated and missing numbers
        # Check each number from 1 to n²
        for i in range(1, n * n + 1):
            if count[i] == 2:
                repeated = i  # Number that appears twice
            elif count[i] == 0:
                missing = i  # Number that appears zero times
        
        # Return array with [repeated, missing]
        return [repeated, missing]

    findMissingAndRepeatedValues = find_missing_and_repeated_values
