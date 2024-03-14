# https://leetcode.com/problems/binary-subarrays-with-sum/


class Solution:
    """930. Binary Subarrays With Sum

    Given a binary array `nums` and an integer `goal`, return *the number of non-empty
    **subarrays** with a sum* `goal`.

    A **subarray** is a contiguous part of the array.

    """

    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        # Initialize the count of subarrays with sum equal to the goal
        count = 0
        
        # Initialize the running total
        total = 0
        
        # Initialize the frequency of prefix sums
        frequency = {0: 1}  

        for num in nums:
            # Increment the running total by the current number
            total += num
            
            # Check if the complement of the current total has been encountered before
            # If yes, add the count of subarrays that sum up to the goal
            count += frequency.get(total - goal, 0)
            
            # Update the frequency of prefix sums
            frequency[total] = frequency.get(total, 0) + 1  

        # Return the count of subarrays with sum equal to the goal
        return count

    numSubarraysWithSum = num_subarrays_with_sum
