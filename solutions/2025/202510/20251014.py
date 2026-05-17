# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/


class Solution:
    """3349. Adjacent Increasing Subarrays Detection I

    Given an array `nums` of `n` integers and an integer `k`, determine whether there
    exist **two** **adjacent** subarrays of length `k` such that both subarrays are
    **strictly** **increasing**. Specifically, check if there are **two** subarrays
    starting at indices `a` and `b` (`a < b`), where:

    * Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly
    increasing**.

    * The subarrays must be **adjacent**, meaning `b = a + k`.

    Return `true` if it is *possible* to find **two** such subarrays, and `false`
    otherwise."""

    def has_increasing_subarrays(self, nums: list[int], k: int) -> bool:
        # Get the length of the input array
        n = len(nums)
        # If the array is too short for two subarrays of length k, return False
        if n < 2 * k:
            return False
        # Create a diff array where diff[j] is 1 if nums[j] < nums[j+1], else 0
        diff = [0] * (n - 1)
        for j in range(n - 1):
            diff[j] = 1 if nums[j] < nums[j + 1] else 0
        # Compute prefix sums: prefix[m] = sum of diff[0] to diff[m-1]
        prefix = [0] * n
        for j in range(n - 1):
            prefix[j + 1] = prefix[j] + diff[j]
        # Check each possible starting index i for the first subarray
        for i in range(n - 2 * k + 1):
            # Check if first subarray (i to i+k-1) is strictly increasing: sum of diff[i to i+k-2] == k-1
            first = prefix[i + k - 1] - prefix[i] == k - 1
            # Check if second subarray (i+k to i+2k-1) is strictly increasing: sum of diff[i+k to i+2k-2] == k-1
            second = prefix[i + 2 * k - 1] - prefix[i + k] == k - 1
            # If both are true, return True
            if first and second:
                return True
        # If no such pair found, return False
        return False

    hasIncreasingSubarrays = has_increasing_subarrays
