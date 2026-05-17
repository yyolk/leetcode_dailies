# https://leetcode.com/problems/find-the-pivot-integer/


class Solution:
    """2485. Find the Pivot Integer

    Given a positive integer `n`, find the **pivot integer** `x` such that:

    * The sum of all elements between `1` and `x` inclusively equals the sum of all
    elements between `x` and `n` inclusively.

    Return *the pivot integer* `x`. If no such integer exists, return `-1`. It is
    guaranteed that there will be at most one pivot index for the given input.

    """

    def pivot_integer(self, n: int) -> int:
        # Using the formula for sum of first n integers to calculate the expected x
        x = (n * (n + 1) / 2) ** 0.5

        # If x is not a whole number, return -1 indicating no pivot integer exists
        if x % 1 != 0:
            return -1
        else:
            # Otherwise, return x as an integer
            return int(x)

    pivotInteger = pivot_integer
