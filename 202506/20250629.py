# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/


class Solution:
    """1498. Number of Subsequences That Satisfy the Given Sum Condition

    You are given an array of integers `nums` and an integer `target`.

    Return *the number of **non-empty** subsequences of* `nums` *such that the sum of
    the minimum and maximum element on it is less or equal to* `target`. Since the
    answer may be too large, return it **modulo** `109 + 7`."""

    def num_subseq(self, nums: list[int], target: int) -> int: ...

    numSubseq = num_subseq
