# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/


class Solution:
    """3736. Minimum Moves to Equal Array Elements III

    You are given an integer array `nums`.

    In one move, you may **increase** the value of any single element `nums[i]` by 1.

    Return the **minimum total** number of **moves** required so that all elements in
    `nums` become **equal**.

    Constraints:

    * `1 <= nums.length <= 100`

    * `1 <= nums[i] <= 100`
    """

    def min_moves(self, nums: list[int]) -> int:
        # Target must be the maximum since we can only increase values.
        target = max(nums)
        # Total moves is the sum of differences to the target.
        return sum(target - x for x in nums)

    minMoves = min_moves
