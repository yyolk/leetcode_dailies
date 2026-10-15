# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/


class Solution:
    """2913. Subarrays Distinct Element Sum of Squares I

    You are given a 0-indexed integer array nums.

    The distinct count of a subarray of nums is defined as:

    * Let nums[i..j] be a subarray of nums consisting of all the indices from
      i to j such that 0 <= i <= j < nums.length. Then the number of distinct
      values in nums[i..j] is called the distinct count of nums[i..j].

    Return the sum of the squares of distinct counts of all subarrays of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Constraints:

    * 1 <= nums.length <= 100

    * 1 <= nums[i] <= 100
    """

    def sum_counts(self, nums: list[int]) -> int:
        # Enumerate every subarray: for each left endpoint expand to the right.
        n = len(nums)
        total = 0
        for left in range(n):
            # Track distinct values seen in the current subarray window.
            seen = set()
            for right in range(left, n):
                seen.add(nums[right])
                # Add the square of the distinct count for this subarray.
                total += len(seen) * len(seen)
        return total

    sumCounts = sum_counts
