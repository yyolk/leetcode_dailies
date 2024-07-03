# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/


class Solution:
    """1509. Minimum Difference Between Largest and Smallest Value in Three Moves

    You are given an integer array `nums`.

    In one move, you can choose one element of `nums` and change it to **any value**.

    Return *the minimum difference between the largest and smallest value of `nums`
    **after performing at most three moves***.

    """

    def min_difference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        # Consider the minimum difference after making at most 3 moves
        # Possible scenarios:
        # 1. Change the 3 largest elements
        diff1 = nums[-4] - nums[0]
        # 2. Change the 3 smallest elements
        diff2 = nums[-1] - nums[3]
        # 3. Change the 2 smallest and 1 largest element
        diff3 = nums[-2] - nums[2]
        # 4. Change the 1 smallest and 2 largest elements
        diff4 = nums[-3] - nums[1]
        
        return min(diff1, diff2, diff3, diff4)

    minDifference = min_difference
