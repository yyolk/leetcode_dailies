# https://leetcode.com/problems/constrained-subsequence-sum/
from collections import deque


class Solution:
    """1425. Constrained Subsequence Sum

    Given an integer array `nums` and an integer `k`, return the maximum sum of a **non-
    empty** subsequence of that array such that for every two **consecutive** integers
    in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <=
    k` is satisfied.

    A *subsequence* of an array is obtained by deleting some number of elements (can be
    zero) from the array, leaving the remaining elements in their original order.
    """

    def constrained_subset_sum(self, nums: list[int], k: int) -> int:
        """The maximum sum of a non-empty subsequence for input array nums, at size k.

        Proposed solution using dynamic programming.

        Args:
            nums (list of int): The input integer array.
            k (int): The expected maximum size of the subsequence.

        Returns:
            int: The maximum sum of a non-empty subsequence from the input nums.
        """
        # Use a deque to maintain the maximum values within the last k elements.
        dq = deque()

        for i in range(len(nums)):
            # Calculate the current value by adding the value at index dq[0] if dq is
            # not empty.
            nums[i] += nums[dq[0]] if dq else 0

            while dq and (i - dq[0] >= k or nums[i] >= nums[dq[-1]]):
                # Remove elements from the left end of the deque that are out of the
                # current window or elements that are less than the current value.
                if nums[i] >= nums[dq[-1]]:
                    dq.pop()
                else:
                    dq.popleft()
                # dq.pop() if nums[i] >= nums[dq[-1]] else dq.popleft()

            if nums[i] > 0:
                dq.append(i)

        # Return the maximum value in the modified nums array, which represents the
        # maximum sum of the non-empty subsequence that satisfies the conditions.
        return max(nums)

    constrainedSubsetSum = constrained_subset_sum
