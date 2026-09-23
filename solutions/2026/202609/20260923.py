# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/


class Solution:
    """1658. Minimum Operations to Reduce X to Zero

    You are given an integer array `nums` and an integer `x`. In one operation,
    you can either remove the leftmost or the rightmost element from the array
    `nums` and subtract its value from `x`. Note that this **modifies** the
    array for future operations.

    Return the **minimum number** of operations to reduce `x` to **exactly** `0`
    if it is possible, otherwise return `-1`.

    Constraints:

    * `1 <= nums.length <= 10^5`
    * `1 <= nums[i] <= 10^4`
    * `1 <= x <= 10^9`
    """

    def min_operations(self, nums: list[int], x: int) -> int:
        """Min prefix+suffix removals summing to x via longest middle subarray."""
        target = sum(nums) - x
        # Need a prefix+suffix that sums to x, i.e. a middle window of sum target.
        if target < 0:
            return -1

        n = len(nums)
        best = -1
        window = 0
        left = 0
        for right, val in enumerate(nums):
            window += val
            # Positive values: shrink until the window is at most target.
            while window > target and left <= right:
                window -= nums[left]
                left += 1
            if window == target:
                best = max(best, right - left + 1)

        return -1 if best < 0 else n - best

    minOperations = min_operations
