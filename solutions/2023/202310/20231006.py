# https://leetcode.com/problems/integer-break/


class Solution:
    """343. Integer Break

    Given an integer `n`, break it into the sum of `k` **positive integers**, where `k >=
    2`, and maximize the product of those integers.

    Return *the maximum product you can get*.
    """

    def integerBreak(self, n: int) -> int:
        """The maximum product you can get from breaking the input into sum of k integers

        Proposed solution using a loop.

        Args:
            n (int): The input integer.

        Returns:
            int: The maximum product of the broken input into sum of k positive
            integers.
        """
        # Handle cases where n < 4 separately
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Initialize max_product with 1, 1 times any number is the number
        max_product = 1

        while n > 4:
            max_product *= 3
            n -= 3

        # At this point, n is either 2 or 3 or 4
        return max_product * n
