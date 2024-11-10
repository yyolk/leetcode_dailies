# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/


class Solution:
    """3097. Shortest Subarray With OR at Least K II

    You are given an array `nums` of **non\\-negative** integers and an integer `k`.

    An array is called **special** if the bitwise `OR` of all of its elements is **at
    least** `k`.

    Return *the length of the **shortest** **special** **non\\-empty** subarray of*
    `nums`, *or return* `-1` *if no special subarray exists*.

    """

    def minimum_subarray_length(self, nums: list[int], k: int) -> int:
        min_length = float("inf")
        # tracks leftmost index for each OR value
        or_to_index = {}

        for right, num in enumerate(nums):
            # Update existing OR values with the new number
            new_or_values = {or_val | num: left for or_val, left in or_to_index.items()}
            # Add the new number itself with its index
            new_or_values[num] = right
            or_to_index = new_or_values

            # Check for valid subarrays
            for or_val, left in or_to_index.items():
                if or_val >= k:
                    min_length = min(min_length, right - left + 1)

        return min_length if min_length != float("inf") else -1

    minimumSubarrayLength = minimum_subarray_length
