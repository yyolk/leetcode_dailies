# https://leetcode.com/problems/count-symmetric-integers/


class Solution:
    """2843.   Count Symmetric Integers

    You are given two positive integers `low` and `high`.

    An integer `x` consisting of `2 * n` digits is **symmetric** if the sum of the first
    `n` digits of `x` is equal to the sum of the last `n` digits of `x`. Numbers with an
    odd number of digits are never symmetric.

    Return *the **number of symmetric** integers in the range* `[low, high]`."""

    def count_symmetric_integers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 == 0:  # Only consider numbers with even number of digits
                n = len(s) // 2
                first_half = s[:n]
                second_half = s[n:]
                sum_first = sum(int(d) for d in first_half)
                sum_second = sum(int(d) for d in second_half)
                if sum_first == sum_second:
                    count += 1
        return count

    countSymmetricIntegers = count_symmetric_integers
