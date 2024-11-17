# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
from collections import deque


class Solution:
    """862. Shortest Subarray with Sum at Least K

    Given an integer array `nums` and an integer `k`, return *the length of the shortest
    non\\-empty **subarray** of* `nums` *with a sum of at least* `k`. If there is no such
    **subarray**, return `-1`.

    A **subarray** is a **contiguous** part of an array.

    """

    def shortest_subarray(self, nums: list[int], k: int) -> int:
        # Calculate prefix sum for efficient sum calculation
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        # Use a deque to keep track of indices in a way that they are always in increasing order of prefix sum
        result = n + 1  # Start with a value larger than the possible maximum subarray length
        dq = deque()

        # +1 because we need to consider the sum up to index n
        for i in range(n + 1):
            # Remove indices from the back of the deque where the sum is larger or equal
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            # Check if there's a subarray where the sum from dq[0] to i is at least k
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            # Add current index to deque
            dq.append(i)

        # If result wasn't updated, there's no subarray with sum >= k
        return result if result <= n else -1

    shortestSubarray = shortest_subarray
