# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/


class Solution:
    """2894. Divisible and Non-divisible Sums Difference

    You are given positive integers `n` and `m`.

    Define two integers as follows:

    * `num1`: The sum of all integers in the range `[1, n]` (both **inclusive**) that
    are **not divisible** by `m`.

    * `num2`: The sum of all integers in the range `[1, n]` (both **inclusive**) that
    are **divisible** by `m`.

    Return *the integer* `num1 - num2`."""

    def difference_of_sums(self, n: int, m: int) -> int: ...

    differenceOfSums = difference_of_sums
