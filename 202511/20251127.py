# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/


class Solution:
    """3381. Maximum Subarray Sum With Length Divisible by K

    You are given an array of integers nums and an integer k.

    Return the maximum sum of a subarray of nums, such that the size of the
    subarray is divisible by k.
    """
    def max_subarray_sum(self, nums: list[int], k: int) -> int:
        # Use a large number for initialization to avoid float issues
        INF = 10**18 + 1
        min_prefix = [INF] * k
        min_prefix[0] = 0  # Prefix sum before index 0
        prefix = 0
        ans = -INF
        for i in range(len(nums)):
            # Accumulate prefix sum up to current index i (0-based)
            prefix += nums[i]
            # Compute modulo for the end position +1
            mod = (i + 1) % k
            # Check if a valid starting prefix exists for this modulo
            if min_prefix[mod] < INF:
                # Candidate sum: current prefix - min prefix with matching modulo
                ans = max(ans, prefix - min_prefix[mod])
            # Update min prefix for this modulo with current prefix
            min_prefix[mod] = min(min_prefix[mod], prefix)
        return ans

    maxSubarraySum = max_subarray_sum