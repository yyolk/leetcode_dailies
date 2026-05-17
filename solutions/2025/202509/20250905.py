# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/


class Solution:
    """2749. Minimum Operations to Make the Integer Zero

    You are given two integers `num1` and `num2`.

    In one operation, you can choose integer `i` in the range `[0, 60]` and subtract `2i
    + num2` from `num1`.

    Return *the integer denoting the **minimum** number of operations needed to make*
    `num1` *equal to* `0`.

    If it is impossible to make `num1` equal to `0`, return `-1`."""

    def make_the_integer_zero(self, num1: int, num2: int) -> int:
        # Loop over possible number of operations m (up to 61 is sufficient since max popcount ~30)
        for m in range(1, 61):
            # Compute the required sum of powers of 2
            s = num1 - m * num2
            # Skip if s cannot be sum of m powers (>= m) or negative
            if s < m:
                continue
            # Compute the number of set bits in s
            pop = bin(s).count("1")
            # Check if s can be expressed as sum of exactly m powers of 2
            if pop <= m:
                # Return the minimal such m
                return m
        # Return -1 if no such m found
        return -1

    makeTheIntegerZero = make_the_integer_zero
