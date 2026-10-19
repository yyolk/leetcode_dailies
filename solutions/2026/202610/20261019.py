# https://leetcode.com/problems/find-target-indices-after-sorting-array/


class Solution:
    """2089. Find Target Indices After Sorting Array

    You are given a 0-indexed integer array nums and a target element target.

    A target index is an index i such that nums[i] == target.

    Return a list of the target indices of nums after sorting nums in
    non-decreasing order. If there are no target indices, return an empty
    list. The returned list must be sorted in increasing order.

    Constraints:

    * 1 <= nums.length <= 100

    * 1 <= nums[i], target <= 100
    """

    def target_indices(self, nums: list[int], target: int) -> list[int]:
        # Count elements strictly less than target (start index after sort).
        less = sum(num < target for num in nums)
        # Count occurrences of target.
        count = sum(num == target for num in nums)
        # Indices form a contiguous range [less, less + count).
        return list(range(less, less + count))

    targetIndices = target_indices
