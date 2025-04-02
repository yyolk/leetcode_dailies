# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/


class Solution:
    """2873. Maximum Value of an Ordered Triplet I

    You are given a **0-indexed** integer array `nums`.

    Return ***the maximum value over all triplets of indices*** `(i, j, k)` *such that*
    `i < j < k`. If all such triplets have a negative value, return `0`.

    The **value of a triplet of indices** `(i, j, k)` is equal to `(nums[i] - nums[j]) *
    nums[k]`."""

    def maximum_triplet_value(self, nums: list[int]) -> int:
        # Get the length of the input array
        n = len(nums)
        
        # Initialize the running maximum with the first element
        running_max = nums[0]  # Tracks the maximum value in nums[0] to nums[j-1]
        
        # Initialize the maximum difference as negative infinity
        max_diff = float("-inf")  # Tracks the maximum (running_max - nums[j]) seen so far
        
        # Initialize the maximum triplet value as 0 (default if all values are negative)
        max_value = 0  # Stores the maximum value of (nums[i] - nums[j]) * nums[k]
        
        # Iterate over k from index 2 to n-1 (since k is the last index in the triplet)
        for k in range(2, n):
            # Compute the difference for j = k-1 using the current running_max
            current_diff = running_max - nums[k-1]  # (max(nums[0] to nums[j-1]) - nums[j])
            
            # Update max_diff if the current difference is larger
            if current_diff > max_diff:
                max_diff = current_diff  # Keep the largest difference seen so far
            
            # Calculate the triplet value using max_diff and nums[k]
            value = max_diff * nums[k]  # (nums[i] - nums[j]) * nums[k] for the best i, j < k
            
            # Update max_value if the computed value is greater
            if value > max_value:
                max_value = value  # Update the maximum triplet value if this is larger
            
            # Update running_max to include nums[k-1] for the next iteration
            running_max = max(running_max, nums[k-1])  # Prepare running_max for the next k
        
        # Return the maximum triplet value (0 if all values were negative)
        return max_value

    maximumTripletValue = maximum_triplet_value
