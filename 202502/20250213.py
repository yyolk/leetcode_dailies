# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
from collections import deque


class Solution:
    """3066. Minimum Operations to Exceed Threshold Value II

    You are given a **0-indexed** integer array `nums`, and an integer `k`.

    In one operation, you will:

    * Take the two smallest integers `x` and `y` in `nums`.

    * Remove `x` and `y` from `nums`.

    * Add `min(x, y) * 2 + max(x, y)` anywhere in the array.

    **Note** that you can only apply the described operation if `nums` contains at least
    two elements.

    Return *the **minimum** number of operations needed so that all elements of the
    array are greater than or equal to* `k`."""

    def min_operations(self, nums: list[int], k: int) -> int:
        nums.sort()
        original = deque(nums)
        merged = deque()
        operations = 0

        def get_min():
            if not original:
                return merged.popleft()
            if not merged:
                return original.popleft()
            if original[0] <= merged[0]:
                return original.popleft()
            else:
                return merged.popleft()

        while True:
            current_min = None
            if original and merged:
                current_min = min(original[0], merged[0])
            elif original:
                current_min = original[0]
            elif merged:
                current_min = merged[0]
            else:
                # No elements left
                break

            if current_min >= k:
                # All remaining elements are >=k
                break

            if (len(original) + len(merged)) < 2:
                # Not possible to proceed
                return -1

            x = get_min()
            y = get_min()

            combined = x * 2 + y
            merged.append(combined)
            operations += 1

        return operations

    minOperations = min_operations
