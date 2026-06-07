# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/


class Solution:
    """2411. Smallest Subarrays With Maximum Bitwise OR

    You are given a **0-indexed** array `nums` of length `n`, consisting of non-negative
    integers. For each index `i` from `0` to `n - 1`, you must determine the size of the
    **minimum sized** non-empty subarray of `nums` starting at `i` (**inclusive**) that
    has the **maximum** possible **bitwise OR**.

    * In other words, let `Bij` be the bitwise OR of the subarray `nums[i...j]`. You
    need to find the smallest subarray starting at `i`, such that bitwise OR of this
    subarray is equal to `max(Bik)` where `i <= k <= n - 1`.

    The bitwise OR of an array is the bitwise OR of all the numbers in it.

    Return *an integer array* `answer` *of size* `n` *where* `answer[i]` *is the length
    of the **minimum** sized subarray starting at* `i` *with **maximum** bitwise OR.*

    A **subarray** is a contiguous non-empty sequence of elements within an array."""

    def smallest_subarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 0:
            return []

        # Precompute max_or for suffixes
        max_or = [0] * n
        max_or[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            max_or[i] = max_or[i + 1] | nums[i]

        # Precompute next_set for each bit
        next_set = [[n] * n for _ in range(32)]
        for b in range(32):
            last = n
            for j in range(n - 1, -1, -1):
                if nums[j] & (1 << b):
                    last = j
                next_set[b][j] = last

        # Compute answer
        answer = [0] * n
        for i in range(n):
            max_pos = i  # at least i
            mor = max_or[i]
            for b in range(32):
                if mor & (1 << b):
                    max_pos = max(max_pos, next_set[b][i])
            answer[i] = max_pos - i + 1

        return answer

    smallestSubarrays = smallest_subarrays
