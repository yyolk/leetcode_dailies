# https://leetcode.com/problems/partition-array-for-maximum-sum/


class Solution:
    """1043. Partition Array for Maximum Sum

    Given an integer array `arr`, partition the array into (contiguous) subarrays of
    length **at most** `k`. After partitioning, each subarray has their values changed
    to become the maximum value of that subarray.

    Return *the largest sum of the given array after partitioning. Test cases are
    generated so that the answer fits in a **32-bit** integer.*

    """

    def max_sum_after_partitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        
        # Initialize an array to store the maximum sum for each position
        dp = [0] * (n + 1)

        # Iterate through the array
        for i in range(1, n + 1):
            max_val = float('-inf')
            
            # Consider subarrays of length at most k
            for j in range(1, min(i, k) + 1):
                # Update the maximum value in the current subarray
                max_val = max(max_val, arr[i - j])
                
                # Update the maximum sum for the current position
                dp[i] = max(dp[i], dp[i - j] + max_val * j)

        # Return the maximum sum after partitioning
        return dp[n]

    maxSumAfterPartitioning = max_sum_after_partitioning
