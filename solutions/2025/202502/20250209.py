# https://leetcode.com/problems/count-number-of-bad-pairs/
from collections import defaultdict


class Solution:
    """2364. Count Number of Bad Pairs

    You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a
    **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

    Return *the total number of **bad pairs** in* `nums`."""

    def count_bad_pairs(self, nums: list[int]) -> int:
        n = len(nums)
        # Total number of pairs (i, j) where i < j
        total_pairs = n * (n - 1) // 2

        # Count the frequency of nums[i] - i
        freq = defaultdict(int)
        for i in range(n):
            freq[nums[i] - i] += 1

        # Calculate the number of good pairs
        good_pairs = 0
        for count in freq.values():
            if count >= 2:
                good_pairs += count * (count - 1) // 2

        # Bad pairs = Total pairs - Good pairs
        bad_pairs = total_pairs - good_pairs
        return bad_pairs

    countBadPairs = count_bad_pairs
