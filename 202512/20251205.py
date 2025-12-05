# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/


class Solution:
    """3432. Count Partitions with Even Sum Difference

    Given an integer array nums of length n, count the partitions at index i
    (0 <= i < n-1) where the difference between the sum of the left subarray
    [0..i] and the right subarray [i+1..n-1] is even.
    """
    def count_partitions(self, nums: list[int]) -> int:
        # diff = left - right = 2*left - total; 2*left is always even
        # → diff is even iff total sum is even → every possible split works
        return (len(nums) - 1) if sum(nums) % 2 == 0 else 0

    countPartitions = count_partitions