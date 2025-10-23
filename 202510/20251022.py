# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/


class Solution:
    """3347. Maximum Frequency of an Element After Performing Operations II

    You are given an integer array `nums` and two integers `k` and `num_operations`.

    You must perform an **operation** `num_operations` times on `nums`, where in each
    operation you:

    * Select an index `i` that was **not** selected in any previous operations.

    * Add an integer in the range `[-k, k]` to `nums[i]`.

    Return the **maximum** possible frequency of any element in `nums` after performing
    the **operations**."""

    def max_frequency(self, nums: list[int], k: int, num_operations: int) -> int:
        if not nums:
            return 0
        # Sort the array for sliding window and binary search
        a = sorted(nums)
        n = len(a)
        # Get frequency of each value
        from collections import Counter

        freq = Counter(nums)
        # Compute max window size where elements differ by at most 2*k
        left = 0
        max_m = 1
        for right in range(n):
            # Shrink window from left if difference exceeds 2*k
            while a[right] - a[left] > 2 * k:
                left += 1
            # Update max window size
            max_m = max(max_m, right - left + 1)
        # Candidate for targeting a new value: min(max_window, num_operations)
        cand_new = min(max_m, num_operations)
        # Initialize max candidate with the new value case
        max_cand = cand_new
        # Use bisect for efficient range queries
        import bisect

        for v in freq:
            # Compute bounds for the window around v
            low = v - k
            high = v + k
            # Find leftmost index >= low
            left_idx = bisect.bisect_left(a, low)
            # Find rightmost index <= high
            right_idx = bisect.bisect_right(a, high) - 1
            # Calculate number of elements in [low, high]
            m_v = right_idx - left_idx + 1 if left_idx <= right_idx else 0
            # Get current frequency of v
            e = freq[v]
            # Compute candidate for this v: min(m_v, e + num_operations)
            cand = min(m_v, e + num_operations)
            # Update max candidate
            max_cand = max(max_cand, cand)
        return max_cand

    maxFrequency = max_frequency
