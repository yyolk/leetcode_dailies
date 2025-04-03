# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/


class Solution:
    """2874. Maximum Value of an Ordered Triplet II

    You are given a **0-indexed** integer array `nums`.

    Return ***the maximum value over all triplets of indices*** `(i, j, k)` *such that*
    `i < j < k`*.* If all such triplets have a negative value, return `0`.

    The **value of a triplet of indices** `(i, j, k)` is equal to `(nums[i] - nums[j]) *
    nums[k]`."""

    def maximum_triplet_value(self, nums: list[int]) -> int:
        n = len(nums)
        # Since constraints guarantee n >= 3, no need to check n < 3
        max_triplet = 0  # Initialize result; return 0 if all values are negative
        current_max = nums[0]  # Tracks max(nums[0] to nums[j-1]) for current j
        max_diff = nums[0] - nums[1]  # Initial max difference for k=2

        # Iterate over k from index 2 to n-1
        for k in range(2, n):
            # Compute triplet value with current max_diff and nums[k]
            triplet_value = max_diff * nums[k]
            if triplet_value > max_triplet:
                max_triplet = triplet_value  # Update if greater
            
            # Update current_max with nums[k-1] (previous element)
            if nums[k - 1] > current_max:
                current_max = nums[k - 1]
            
            # Update max_diff with new difference using current_max and nums[k]
            diff = current_max - nums[k]
            if diff > max_diff:
                max_diff = diff
        
        return max_triplet

    maximumTripletValue = maximum_triplet_value
