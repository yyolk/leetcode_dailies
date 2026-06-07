# https://leetcode.com/problems/valid-triangle-number/


class Solution:
    """611. Valid Triangle Number

    Given an integer array `nums`, return *the number of triplets chosen from the array
    that can make triangles if we take them as side lengths of a triangle*."""

    def triangle_number(self, nums: list[int]) -> int:
        # Early return if fewer than 3 elements
        if len(nums) < 3:
            return 0
        # Sort the array to enable two-pointer technique
        nums.sort()
        # Get the length of the array
        n = len(nums)
        # Initialize count of valid triplets
        count = 0
        # Iterate over possible largest sides (k from 2 to n-1)
        for k in range(2, n):
            # Initialize two pointers for pairs before k
            left = 0
            right = k - 1
            # Use two pointers to count pairs where nums[left] + nums[right] > nums[k]
            while left < right:
                # If sum > nums[k], all pairs from left to right-1 with this right are valid
                if nums[left] + nums[right] > nums[k]:
                    # Add the number of valid left positions for this right
                    count += right - left
                    # Move right inward to check smaller sums
                    right -= 1
                else:
                    # Move left outward to increase the sum
                    left += 1
        # Return the total count of valid triplets
        return count

    triangleNumber = triangle_number
