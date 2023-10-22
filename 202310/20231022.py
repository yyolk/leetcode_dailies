# https://leetcode.com/problems/maximum-score-of-a-good-subarray/


class Solution:
    """1793. Maximum Score of a Good Subarray

    You are given an array of integers `nums` **(0-indexed)** and an integer `k`.

    The **score** of a subarray `(i, j)` is defined as `min(nums[i], nums[i+1], ...,
    nums[j]) * (j - i + 1)`. A **good** subarray is a subarray where `i <= k <= j`.

    Return *the maximum possible **score** of a **good** subarray.*
    """

    def maximum_score(self, nums: List[int], k: int) -> int:
        ...

    maximumScore = maximum_score
