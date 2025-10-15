# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/


class Solution:
    """3350. Adjacent Increasing Subarrays Detection II

    Given an array `nums` of `n` integers, your task is to find the **maximum** value of
    `k` for which there exist **two** adjacent subarrays of length `k` each, such that
    both subarrays are **strictly** **increasing**. Specifically, check if there are
    **two** subarrays of length `k` starting at indices `a` and `b` (`a < b`), where:

    * Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly
    increasing**.

    * The subarrays must be **adjacent**, meaning `b = a + k`.

    Return the **maximum** *possible* value of `k`.

    A **subarray** is a contiguous **non-empty** sequence of elements within an array.
    """

    def max_increasing_subarrays(self, nums: list[int]) -> int:
        # Get length of nums
        n = len(nums)
        # If n < 2, no possible k >= 1
        if n < 2:
            return 0
        
        # Binary search for maximum k
        low, high = 0, n // 2
        
        # Helper function to check if k is possible
        def can_have_k(k: int) -> bool:
            # If 2k > n, impossible
            if 2 * k > n:
                return False
            # Compute inc array: 1 if nums[i] < nums[i+1], else 0
            inc = [0] * (n - 1)
            for i in range(n - 1):
                inc[i] = 1 if nums[i] < nums[i + 1] else 0
            # Compute prefix sums for inc
            prefix = [0] * (n)
            for i in range(1, n):
                prefix[i] = prefix[i - 1] + inc[i - 1]
            # Check each possible starting index a
            for a in range(n - 2 * k + 1):
                # Sum for first subarray: must be k-1
                sum1 = prefix[a + k - 1] - prefix[a]
                # Sum for second subarray: must be k-1
                sum2 = prefix[a + 2 * k - 1] - prefix[a + k]
                if sum1 == k - 1 and sum2 == k - 1:
                    return True
            return False
        
        # Perform binary search to find max k
        while low < high:
            # Bias towards higher values
            mid = (low + high + 1) // 2
            if can_have_k(mid):
                low = mid
            else:
                high = mid - 1
        return low

    maxIncreasingSubarrays = max_increasing_subarrays
