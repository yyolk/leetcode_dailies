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

    def difference_of_sums(self, n: int, m: int) -> int:
        # Calculate the total sum of numbers from 1 to n
        sum_all = n * (n + 1) // 2

        # Calculate the number of multiples of m up to n
        k = n // m

        # Calculate the sum of all numbers divisible by m (num2)
        num2 = m * k * (k + 1) // 2

        # Calculate the sum of all numbers not divisible by m (num1)
        num1 = sum_all - num2

        # Return the difference num1 - num2
        return num1 - num2

    differenceOfSums = difference_of_sums
