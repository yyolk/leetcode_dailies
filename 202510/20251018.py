# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/


class Solution:
    """3397. Maximum Number of Distinct Elements After Operations

    You are given an integer array `nums` and an integer `k`.

    You are allowed to perform the following **operation** on each element of the array
    **at most** *once*:

    * Add an integer in the range `[-k, k]` to the element.

    Return the **maximum** possible number of **distinct** elements in `nums` after
    performing the **operations**."""

    def max_distinct_elements(self, nums: list[int], k: int) -> int:
        # Sort the array to process elements in increasing order
        nums.sort()
        # Initialize result counter for distinct elements
        res = 0
        # Set initial smallest possible value just before the first element's lower bound
        smallest_elem = nums[0] - k - 1

        # Iterate through each sorted element
        for num in nums:
            # Check if the current element's upper bound allows placement after current smallest
            if num + k > smallest_elem:
                # Increment the count of distinct elements
                res += 1
                # Update smallest to the next available slot: max of next after current or element's lower bound
                smallest_elem = max(smallest_elem + 1, num - k)

        # Return the maximum number of distinct elements
        return res

    maxDistinctElements = max_distinct_elements
