# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/


class Solution:
    """1304. Find N Unique Integers Sum up to Zero

    Given an integer `n`, return **any** array containing `n` **unique** integers such
    that they add up to `0`."""

    def sum_zero(self, n: int) -> list[int]:
        # Initialize an empty list to hold the unique integers
        result = []
        # Loop to add pairs of positive and negative integers that cancel each other
        for i in range(1, n // 2 + 1):
            # Add the positive integer
            result.append(i)
            # Add its negative counterpart to cancel the sum
            result.append(-i)
        # For odd n, add 0 to reach n elements without affecting the sum
        if n % 2 == 1:
            result.append(0)
        # Return the list of n unique integers summing to 0
        return result

    sumZero = sum_zero
