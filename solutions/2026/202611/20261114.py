# https://leetcode.com/problems/minimum-positive-sum-subarray/


class Solution:
    """3364. Minimum Positive Sum Subarray

    You are given an integer array nums and two integers l and r. Your task is
    to find the minimum sum of a subarray whose size is between l and r
    (inclusive) and whose sum is greater than 0.

    Return the minimum sum of such a subarray. If no such subarray exists,
    return -1.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Constraints:

    * 1 <= nums.length <= 100

    * 1 <= l <= r <= nums.length

    * -1000 <= nums[i] <= 1000
    """

    def minimum_sum_subarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_positive = float("inf")
        # Check every allowed window length.
        for length in range(l, r + 1):
            # Initial sum of the first window of this length.
            window_sum = sum(nums[:length])
            if window_sum > 0:
                min_positive = min(min_positive, window_sum)
            # Slide the fixed-length window to the right.
            for i in range(length, n):
                window_sum += nums[i] - nums[i - length]
                if window_sum > 0:
                    min_positive = min(min_positive, window_sum)
        return int(min_positive) if min_positive != float("inf") else -1

    minimumSumSubarray = minimum_sum_subarray
