# https://leetcode.com/problems/largest-perimeter-triangle/


class Solution:
    """976. Largest Perimeter Triangle

    Given an integer array `nums`, return *the largest perimeter of a triangle with a
    non-zero area, formed from three of these lengths*. If it is impossible to form any
    triangle of a non-zero area, return `0`."""

    def largest_perimeter(self, nums: list[int]) -> int:
        # Sort the list in descending order to prioritize larger perimeters
        nums.sort(reverse=True)
        # Iterate through possible triplets starting from the largest
        for i in range(len(nums) - 2):
            # Check triangle inequality: largest side < sum of other two
            if nums[i] < nums[i + 1] + nums[i + 2]:
                # Return the perimeter if condition is met
                return nums[i] + nums[i + 1] + nums[i + 2]
        # Return 0 if no valid triangle found
        return 0

    largestPerimeter = largest_perimeter
