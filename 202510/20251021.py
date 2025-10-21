# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/


class Solution:
    """3346. Maximum Frequency of an Element After Performing Operations I

    You are given an integer array `nums` and two integers `k` and `num_operations`.

    You must perform an **operation** `num_operations` times on `nums`, where in each
    operation you:

    * Select an index `i` that was **not** selected in any previous operations.

    * Add an integer in the range `[-k, k]` to `nums[i]`.

    Return the **maximum** possible frequency of any element in `nums` after performing
    the **operations**."""

    def max_frequency(self, nums: list[int], k: int, num_operations: int) -> int: ...

    maxFrequency = max_frequency
