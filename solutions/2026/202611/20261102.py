# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/


class Solution:
    """462. Minimum Moves to Equal Array Elements II

    Given an integer array `nums` of size `n`, return the minimum number of
    moves required to make all array elements equal.

    In one move, you can increment or decrement an element of the array by 1.

    Test cases are designed so that the answer will fit in a 32-bit integer.
    """

    def min_moves2(self, nums: list[int]) -> int:
        # Sort so the median is at the middle index.
        nums.sort()
        # Median minimizes the sum of absolute deviations.
        median = nums[len(nums) // 2]
        # Total moves is the sum of |num - median| for all elements.
        return sum(abs(num - median) for num in nums)

    minMoves2 = min_moves2
