# https://leetcode.com/problems/maximum-erasure-value/


class Solution:
    """1695. Maximum Erasure Value

    You are given an array of positive integers `nums` and want to erase a subarray
    containing **unique elements**. The **score** you get by erasing the subarray is
    equal to the **sum** of its elements.

    Return *the **maximum score** you can get by erasing **exactly one** subarray.*

    An array `b` is called to be a subarray of `a` if it forms a contiguous subsequence
    of `a`, that is, if it is equal to `a[l],a[l+1],...,a[r]` for some `(l,r)`."""

    def maximum_unique_subarray(self, nums: list[int]) -> int:
        # Check if the input array is empty
        if not nums:
            # Return 0 for empty array
            return 0
        # Initialize left pointer for sliding window
        left = 0
        # Initialize variable to track maximum sum of unique subarray
        max_sum = 0
        # Initialize variable to track current subarray sum
        current_sum = 0
        # Initialize set to track unique elements in current window
        seen = set()
        # Iterate through array with right pointer
        for right in range(len(nums)):
            # While current element is already in set (duplicate found)
            while nums[right] in seen:
                # Subtract leftmost element from current sum
                current_sum -= nums[left]
                # Remove leftmost element from set
                seen.remove(nums[left])
                # Move left pointer forward
                left += 1
            # Add current element to set
            seen.add(nums[right])
            # Add current element to current sum
            current_sum += nums[right]
            # Update maximum sum if current sum is larger
            max_sum = max(max_sum, current_sum)
        # Return the maximum sum found
        return max_sum

    maximumUniqueSubarray = maximum_unique_subarray
