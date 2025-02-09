# https://leetcode.com/problems/count-number-of-bad-pairs/


class Solution:
    """2364. Count Number of Bad Pairs

    You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a
    **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

    Return *the total number of **bad pairs** in* `nums`."""

    def count_bad_pairs(self, nums: list[int]) -> int: ...

    countBadPairs = count_bad_pairs
