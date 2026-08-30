# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/


class Solution:
    """2091. Removing Minimum and Maximum From Array

    You are given a 0-indexed array of distinct integers nums.

    There is an element in nums that has the lowest value and an element that has
    the highest value. We call them the minimum and maximum respectively. Your
    goal is to remove both these elements from the array.

    A deletion is defined as either removing an element from the front of the
    array or removing an element from the back of the array.

    Return the minimum number of deletions it would take to remove both the
    minimum and maximum element from the array.

    Constraints:

    * 1 <= nums.length <= 105

    * -105 <= nums[i] <= 105

    * The integers in nums are distinct.
    """

    def minimum_deletions(self, nums: list[int]) -> int:
        """Return the fewest front/back deletions to remove min and max."""
        n = len(nums)
        # Single element is both min and max: one deletion.
        if n == 1:
            return 1

        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))
        left = min(min_i, max_i)
        right = max(min_i, max_i)

        # Both from the front, both from the back, or one from each end.
        from_front = right + 1
        from_back = n - left
        from_both_ends = (left + 1) + (n - right)
        return min(from_front, from_back, from_both_ends)

    minimumDeletions = minimum_deletions
