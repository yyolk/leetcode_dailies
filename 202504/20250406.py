# https://leetcode.com/problems/largest-divisible-subset/


class Solution:
    """368. Largest Divisible Subset

    Given a set of **distinct** positive integers `nums`, return the largest subset
    `answer` such that every pair `(answer[i], answer[j])` of elements in this subset
    satisfies:

    * `answer[i] % answer[j] == 0`, or

    * `answer[j] % answer[i] == 0`

    If there are multiple solutions, return any of them."""

    def largest_divisible_subset(self, nums: list[int]) -> list[int]:
        # Handle empty input case (though constraints ensure n >= 1)
        if not nums:
            return []
        
        # Sort the array in ascending order to simplify divisibility checks
        nums.sort()
        n = len(nums)
        
        # dp[i] represents the length of the longest divisible subset ending at nums[i]
        dp = [1] * n
        # prev[i] stores the previous index in the optimal subset ending at nums[i]
        prev = [-1] * n
        
        # Variables to track the maximum length and its ending index
        max_len = 1
        max_idx = 0
        
        # Fill the dp array using dynamic programming
        for i in range(1, n):
            for j in range(i):
                # Check if nums[j] divides nums[i]
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    # Update max_len and max_idx if a longer subset is found
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_idx = i
        
        # Reconstruct the largest divisible subset
        result = []
        current_idx = max_idx
        while current_idx != -1:
            result.append(nums[current_idx])
            current_idx = prev[current_idx]
        
        # Return the subset in ascending order (reverse since we built it backwards)
        return result[::-1]

    largestDivisibleSubset = largest_divisible_subset
