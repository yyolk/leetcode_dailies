# https://leetcode.com/problems/number-of-ways-to-split-array/


class Solution:
    """2270. Number of Ways to Split Array

    You are given a **0-indexed** integer array `nums` of length `n`.

    `nums` contains a **valid split** at index `i` if the following are true:

    * The sum of the first `i + 1` elements is **greater than or equal to** the sum of
    the last `n - i - 1` elements.

    * There is **at least one** element to the right of `i`. That is, `0 <= i < n - 1`.

    Return *the number of **valid splits** in* `nums`."""

    def ways_to_split_array(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum

            if left_sum >= right_sum:
                valid_splits += 1

        return valid_splits

    waysToSplitArray = ways_to_split_array
