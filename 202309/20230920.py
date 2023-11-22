# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/


class Solution:
    """1658. Minimum Operations to Reduce X to Zero

    You are given an integer array `nums` and an integer `x`. In one operation, you can
    either remove the leftmost or the rightmost element from the array `nums` and subtract
    its value from `x`. Note that this **modifies** the array for future operations.

    Return *the **minimum number** of operations to reduce* `x` *to **exactly*** `0` *if it
    is possible**, otherwise, return* `-1`.
    """

    def minOperations(self, nums: list[int], x: int) -> int:
        """The minimum number of operations to reduce x to exactly 0

        Proposed solution

        Args:
            nums (list of int): an integer array that leftmost or rightmost items can be
                subtracted from x to reduce it to 0
            x (int): work on number to determine the minimum operations to reduce to 0

        Returns:
            int: the minimum number of operations to reduce x to 0, -1 if not possible
        """
        total_sum = sum(nums)
        target = total_sum - x
        n = len(nums)

        # Input x is larger than what we can make subtracting _all_ nums
        if target < 0:
            return -1

        left, right = 0, 0
        current_sum = 0
        # Instantiate min_operations which we'll continuously run min(new, this) against
        min_operations = float("inf")

        # Iterate through nums, starting from the right
        while right < n:
            current_sum += nums[right]
            # When current_sum >= target, iterate through nums, starting from the left
            while current_sum >= target:
                # When current_sum matches the target...
                if current_sum == target:
                    # ...update min_operations with the minimum of its current value
                    # and the length of the remaining part of the array (nums - subarray)
                    min_operations = min(min_operations, n - (right - left + 1))
                # Ensure we're picking out a number within our nums list indices
                if left < n:
                    current_sum -= nums[left]
                    left += 1
                # If not, move on
                else:
                    break
            right += 1

        # We've found a valid min_operations if our min_operations changed
        return min_operations if min_operations != float("inf") else -1
