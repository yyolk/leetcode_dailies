# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/


class Solution:
    """2958. Length of Longest Subarray With at Most K Frequency

    You are given an integer array `nums` and an integer `k`.

    The **frequency** of an element `x` is the number of times it occurs in an array.

    An array is called **good** if the frequency of each element in this array is **less
    than or equal** to `k`.

    Return *the length of the **longest** **good** subarray of* `nums`*.*

    A **subarray** is a contiguous non-empty sequence of elements within an array.

    Constraints:

    * `1 <= nums.length <= 105`

    * `1 <= nums[i] <= 109`

    * `1 <= k <= nums.length`"""

    def max_subarray_length(self, nums: list[int], k: int) -> int:
        """Return the longest subarray where every value appears at most k times."""
        counts: dict[int, int] = {}
        left = 0
        best = 0

        for right, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1

            while counts[value] > k:
                left_value = nums[left]
                counts[left_value] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best

    maxSubarrayLength = max_subarray_length
