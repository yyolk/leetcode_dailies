# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/


class Solution:
    """2962. Count Subarrays Where Max Element Appears at Least K Times

    You are given an integer array `nums` and a **positive** integer `k`.

    Return *the number of subarrays where the **maximum** element of* `nums` *appears
    **at least*** `k` *times in that subarray.*

    A **subarray** is a contiguous sequence of elements within an array."""

    def count_subarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_val = max(nums)
        prefix = [0] * (n + 1)

        # Build prefix sum array for the count of max_val
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (1 if nums[i - 1] == max_val else 0)

        answer = 0
        p = 0

        # For each ending index r, count the number of valid starting indices
        for r in range(n):
            while p < n + 1 and prefix[p] <= prefix[r + 1] - k:
                p += 1
            answer += p

        return answer

    countSubarrays = count_subarrays
