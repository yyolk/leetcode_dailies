# https://leetcode.com/problems/largest-divisible-subset/


class Solution:
    """368. Largest Divisible Subset

    Given a set of **distinct** positive integers `nums`, return the largest subset
    `answer` such that every pair `(answer[i], answer[j])` of elements in this subset
    satisfies:

    * `answer[i] % answer[j] == 0`, or

    * `answer[j] % answer[i] == 0`

    If there are multiple solutions, return any of them.

    """

    def largest_divisible_subset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        # Initialize dynamic programming arrays
        dp = [1] * n  # Length of the largest divisible subset ending at nums[i]
        prev_index = [-1] * n  # Previous index for constructing the result

        max_len, max_idx = 1, 0  # Length and index of the largest divisible subset

        # Dynamic programming
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # Reconstruct the largest divisible subset
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev_index[max_idx]

        return result[::-1]

    largestDivisibleSubset = largest_divisible_subset
