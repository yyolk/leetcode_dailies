# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores


class Solution:
    """1984. Minimum Difference Between Highest and Lowest of K Scores

    You are given a 0-indexed integer array nums, where nums[i] represents the
    score of the ith student. You are also given an integer k.

    Pick the scores of any k students from the array so that the difference
    between the highest and the lowest of the k scores is minimized.

    Return the minimum possible difference.
    """
    def minimum_difference(self, nums: list[int], k: int) -> int:
        # Sort the array to enable sliding window for minimal range
        nums.sort()
        # Initialize minimum difference to a large value
        min_diff = float('inf')
        # Slide window of size k over sorted array
        for i in range(len(nums) - k + 1):
            # Compute difference for current window
            diff = nums[i + k - 1] - nums[i]
            # Update minimum if smaller
            if diff < min_diff:
                min_diff = diff
        return min_diff

    minimumDifference = minimum_difference