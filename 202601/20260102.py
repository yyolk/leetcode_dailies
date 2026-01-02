# https://leetcode.com/problems/n-repeated-element-in-size-2n-array


class Solution:
    """961. N-Repeated Element in Size 2N Array

    You are given an integer array nums with the following properties:

    - nums.length == 2 * n.
    - nums contains n + 1 unique elements.
    - Exactly one element of nums is repeated n times.

    Return the element that is repeated n times.
    """
    def repeated_n_times(self, nums: list[int]) -> int:
        # Set to track elements seen so far; others appear once, repeated appears n times
        seen = set()
        # Iterate through the array once
        for num in nums:
            # First duplicate encountered must be the one repeated n times
            if num in seen:
                return num
            # Mark element as seen
            seen.add(num)

    repeatedNTimes = repeated_n_times