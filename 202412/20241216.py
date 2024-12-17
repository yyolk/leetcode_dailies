# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/


class Solution:
    """3264. Final Array State After K Multiplication Operations I

    You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

    You need to perform `k` operations on `nums`. In each operation:

    * Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the
    minimum value, select the one that appears **first**.

    * Replace the selected minimum value `x` with `x * multiplier`.

    Return an integer array denoting the *final state* of `nums` after performing all
    `k` operations."""

    def get_final_state(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        # Convert nums to a list if it isn't already, to allow for index manipulation
        nums = list(nums)

        for _ in range(k):
            # Find the index of the first occurrence of the minimum value
            min_value = min(nums)
            min_index = nums.index(min_value)

            # Multiply the minimum value by the multiplier
            nums[min_index] *= multiplier

        return nums

    getFinalState = get_final_state
