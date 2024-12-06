# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/


class Solution:
    """2554. Maximum Number of Integers to Choose From a Range I

    You are given an integer array `banned` and two integers `n` and `max_sum`. You are
    choosing some number of integers following the below rules:

    * The chosen integers have to be in the range `[1, n]`.

    * Each integer can be chosen **at most once**.

    * The chosen integers should not be in the array `banned`.

    * The sum of the chosen integers should not exceed `max_sum`.

    Return *the **maximum** number of integers you can choose following the mentioned
    rules*."""

    def max_count(self, banned: list[int], n: int, max_sum: int) -> int: ...

    maxCount = max_count
