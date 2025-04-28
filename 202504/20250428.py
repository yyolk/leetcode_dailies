# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/


class Solution:
    """2302. Count Subarrays With Score Less Than K

    The **score** of an array is defined as the **product** of its sum and its length.

    * For example, the score of `[1, 2, 3, 4, 5]` is `(1 + 2 + 3 + 4 + 5) * 5 = 75`.

    Given a positive integer array `nums` and an integer `k`, return *the **number of
    non-empty subarrays** of* `nums` *whose score is **strictly less** than* `k`.

    A **subarray** is a contiguous sequence of elements within an array."""

    def count_subarrays(self, nums: list[int], k: int) -> int: ...

    countSubarrays = count_subarrays
