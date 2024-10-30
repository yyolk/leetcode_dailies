# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/


class Solution:
    """1671. Minimum Number of Removals to Make Mountain Array

    You may recall that an array `arr` is a **mountain array** if and only if:

    * `arr.length >= 3`

    * There exists some index `i` (**0\\-indexed**) with `0 < i < arr.length - 1` such
    that:

            + `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`

            + `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

    Given an integer array `nums`\u200b\u200b\u200b, return *the **minimum** number of elements to
    remove to make* `nums\u200b\u200b\u200b`*a **mountain array**.*

    """

    def minimum_mountain_removals(self, nums: list[int]) -> int:
        if len(nums) < 3:
            # Cannot form a mountain with fewer than 3 elements
            return 0

        def longest_increasing_subsequence(arr):
            dp = [1] * len(arr)
            for i in range(1, len(arr)):
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp

        # LIS from left to right
        left_to_right = longest_increasing_subsequence(nums)

        # LIS from right to left
        nums.reverse()
        right_to_left = longest_increasing_subsequence(nums)
        right_to_left.reverse()  # Correct the order back

        # Find the peak where both left and right parts form an increasing and decreasing sequence
        max_len = 0
        # Skipping first and last to ensure mountain property
        for i in range(1, len(nums) - 1):
            # Must be peak
            if left_to_right[i] > 1 and right_to_left[i] > 1:
                # -1 to avoid counting peak twice
                current_len = left_to_right[i] + right_to_left[i] - 1
                max_len = max(max_len, current_len)

        # Total elements minus the length of the longest mountain array
        return len(nums) - max_len

    minimumMountainRemovals = minimum_mountain_removals
