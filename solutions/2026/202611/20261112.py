# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/


class Solution:
    """3105. Longest Strictly Increasing or Strictly Decreasing Subarray

    You are given an array of integers `nums`. Return *the length of the
    **longest** subarray of* `nums` *which is either **strictly increasing**
    or **strictly decreasing***.

    Constraints:

    * `1 <= nums.length <= 50`

    * `1 <= nums[i] <= 50`
    """

    def longest_monotonic_subarray(self, nums: list[int]) -> int:
        """Return length of longest strictly mono subarray.

        Track current increasing and decreasing streak lengths in one pass.
        Reset the opposite streak when the direction changes or equals.

        Args:
            nums (list of int): Input array of integers.

        Returns:
            int: Length of the longest valid subarray.
        """
        if not nums:
            return 0
        # At least one element is always valid.
        longest = 1
        incr = 1
        decr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Continue increasing streak; reset decreasing.
                incr += 1
                decr = 1
            elif nums[i] < nums[i - 1]:
                # Continue decreasing streak; reset increasing.
                decr += 1
                incr = 1
            else:
                # Equal elements break both streaks.
                incr = 1
                decr = 1
            longest = max(longest, incr, decr)
        return longest

    longestMonotonicSubarray = longest_monotonic_subarray
