# https://leetcode.com/problems/maximum-width-ramp/


class Solution:
    """962. Maximum Width Ramp

    A **ramp** in an integer array `nums` is a pair `(i, j)` for which `i < j` and
    `nums[i] <= nums[j]`. The **width** of such a ramp is `j - i`.

    Given an integer array `nums`, return *the maximum width of a **ramp** in* `nums`.
    If there is no **ramp** in `nums`, return `0`.

    """

    def max_width_ramp(self, nums: list[int]) -> int:
        # Use a stack to keep indices of nums where nums is in non-increasing order
        stack = []
        n = len(nums)
        
        # First pass: build the stack with indices
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        # Second pass: find the maximum width ramp by moving from right to left
        max_width = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                # If current element can form a ramp with the top of stack
                max_width = max(max_width, i - stack.pop())
        
        return max_width

    maxWidthRamp = max_width_ramp
