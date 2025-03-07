# https://leetcode.com/problems/closest-prime-numbers-in-range/


class Solution:
    """2523. Closest Prime Numbers in Range

    Given two positive integers `left` and `right`, find the two integers `num1` and
    `num2` such that:

    * `left <= num1 < num2 <= right` .

    * Both `num1` and `num2` are prime numbers.

    * `num2 - num1` is the **minimum** amongst all other pairs satisfying the above
    conditions.

    Return the positive integer array `ans = [num1, num2]`. If there are multiple pairs
    satisfying these conditions, return the one with the **smallest** `num1` value. If
    no such numbers exist, return `[-1, -1]`*.*"""

    def closest_primes(self, left: int, right: int) -> list[int]: ...

    closestPrimes = closest_primes
