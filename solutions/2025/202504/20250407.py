# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    """416. Partition Equal Subset Sum

    Given an integer array `nums`, return `true` *if you can partition the array into
    two subsets such that the sum of the elements in both subsets is equal or* `false`
    *otherwise*."""

    def can_partition(self, nums: list[int]) -> bool:
        # Step 1: Calculate the total sum
        total_sum = sum(nums)

        # Step 2: If sum is odd, partitioning is impossible
        if total_sum % 2 != 0:
            return False

        # Step 3: Set target as half of the total sum
        target = total_sum // 2

        # Step 4: Initialize DP array
        dp = [False] * (target + 1)
        dp[0] = True  # Sum 0 is achievable with an empty subset

        # Step 5: Process each number in nums
        for num in nums:
            # Update dp from target down to num
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        # Step 6: Return whether target sum is achievable
        return dp[target]

    canPartition = can_partition
