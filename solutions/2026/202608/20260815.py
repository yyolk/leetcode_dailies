# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/


class Solution:
    """3702. Longest Subsequence With Non-Zero Bitwise XOR

    You are given an integer array `nums`.

    Return the length of the **longest subsequence** in `nums` whose bitwise **XOR** is
    **non-zero**. If no such **subsequence** exists, return 0.

    Constraints:

    * `1 <= nums.length <= 105`

    * `0 <= nums[i] <= 109`"""

    def longest_subsequence(self, nums: list[int]) -> int:
        """Return the maximum subsequence length with non-zero XOR."""
        xor_all = 0
        has_non_zero = False
        for value in nums:
            xor_all ^= value
            if value != 0:
                has_non_zero = True

        if xor_all != 0:
            return len(nums)

        if has_non_zero:
            return len(nums) - 1

        return 0

    longestSubsequence = longest_subsequence
