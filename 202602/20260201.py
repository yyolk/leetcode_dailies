# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i

class Solution:
    """3010. Divide an Array Into Subarrays With Minimum Cost I
    
    You are given an array of integers nums of length n.
    The cost of a subarray is the value of its first element.
    For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.
    You need to divide nums into 3 disjoint contiguous subarrays.
    Return the minimum possible sum of the costs of these subarrays.
    """
    def minimum_cost(self, nums: list[int]) -> int:
        # Cost of first subarray is always nums[0]
        # Minimize sum of starting elements of second and third subarrays
        # by selecting the two smallest values from nums[1:]
        
        # Initialize with first two candidates
        first_min = min(nums[1], nums[2])
        second_min = max(nums[1], nums[2])
        
        # Update with remaining elements if smaller
        for num in nums[3:]:
            if num < first_min:
                second_min = first_min
                first_min = num
            elif num < second_min:
                second_min = num
        
        return nums[0] + first_min + second_min

    minimumCost = minimum_cost