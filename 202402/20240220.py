# https://leetcode.com/problems/missing-number/


class Solution:
    """268. Missing Number

    Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return
    *the only number in the range that is missing from the array.*

    """

    def missing_number(self, nums: list[int]) -> int:
        # Calculate the expected sum of numbers in the range [0, n]
        n = len(nums)
        expected_sum = n * (n + 1) // 2

        # Calculate the actual sum of numbers in the given array
        actual_sum = sum(nums)

        # The difference between the expected sum and the actual sum is the missing number
        return expected_sum - actual_sum

    missingNumber = missing_number
