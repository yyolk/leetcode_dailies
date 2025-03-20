# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/


class Solution:
    """3191. Minimum Operations to Make Binary Array Elements Equal to One I

    You are given a binary array `nums`.

    You can do the following operation on the array **any** number of times (possibly
    zero):

    * Choose **any** 3 **consecutive** elements from the array and **flip** **all** of
    them.

    **Flipping** an element means changing its value from 0 to 1, and from 1 to 0.

    Return the **minimum** number of operations required to make all elements in `nums`
    equal to 1. If it is impossible, return -1."""

    def min_operations(self, nums: list[int]) -> int:
        n = len(nums)
        x_prev2 = 0  # Represents x[i-2], initially for positions before 0
        x_prev1 = 0  # Represents x[i-1], initially for positions before 0
        count = 0    # Counts the number of operations

        # Process positions from 0 to n-3 to determine operations
        for i in range(n - 2):
            # Calculate if operation at i is needed to make nums[i] = 1
            # x_i is 1 if total flips at i must be odd (for 0->1) or even (for 1->1)
            x_i = (1 - nums[i] - x_prev2 - x_prev1) % 2
            if x_i == 1:
                count += 1
            # Shift previous operation variables
            x_prev2 = x_prev1
            x_prev1 = x_i

        # Check if the last two positions can be made 1 with the operations chosen
        sum_n2 = (x_prev2 + x_prev1) % 2  # Total flips at position n-2
        sum_n1 = x_prev1                  # Total flips at position n-1 (always x_{n-3})
        
        # If total flips make nums[n-2] and nums[n-1] become 1, solution is valid
        if sum_n2 == 1 - nums[n - 2] and sum_n1 == 1 - nums[n - 1]:
            return count
        else:
            return -1

    minOperations = min_operations
