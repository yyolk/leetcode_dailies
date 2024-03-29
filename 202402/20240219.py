# https://leetcode.com/problems/power-of-two/


class Solution:
    """231. Power of Two

    Given an integer `n`, return *`true` if it is a power of two. Otherwise, return
    `false`*.

    An integer `n` is a power of two, if there exists an integer `x` such that `n ==
    2x`.

    """

    def is_power_of_two(self, n: int) -> bool:
        """Uses bitwise operations.

        As binary representation with powers of 2 have a unique pattern.
        """
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    isPowerOfTwo = is_power_of_two
