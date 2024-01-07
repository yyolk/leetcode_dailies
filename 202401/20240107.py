# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/


class Solution:
    """446. Arithmetic Slices II - Subsequence

    Given an integer array `nums`, return *the number of all the **arithmetic
    subsequences** of* `nums`.

    A sequence of numbers is called arithmetic if it consists of **at least three
    elements** and if the difference between any two consecutive elements is the same.

    * For example, `[1, 3, 5, 7, 9]`, `[7, 7, 7, 7]`, and `[3, -1, -5, -9]` are
    arithmetic sequences.

    * For example, `[1, 1, 2, 5, 7]` is not an arithmetic sequence.

    A **subsequence** of an array is a sequence that can be formed by removing some
    elements (possibly none) of the array.

    * For example, `[2,5,10]` is a subsequence of `[1,2,1,**2**,4,1,**5**,**10**]`.

    The test cases are generated so that the answer fits in **32-bit** integer.
    """

    def number_of_arithmetic_slices(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0  # Total number of arithmetic subsequences
        
        # dp[i][diff] represents the number of arithmetic subsequences ending at index
        # i with difference diff.
        dp = [{} for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Number of subsequences ending at index j with difference diff
                count = dp[j].get(diff, 0)
                result += count
                dp[i][diff] = dp[i].get(diff, 0) + count + 1

        return result

    numberOfArithmeticSlices = number_of_arithmetic_slices
