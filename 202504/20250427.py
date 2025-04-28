# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/


class Solution:
    """3392. Count Subarrays of Length Three With a Condition

    Given an integer array `nums`, return the number of subarrays of length 3 such that
    the sum of the first and third numbers equals *exactly* half of the second number.
    """

    def count_subarrays(self, nums: list[int]) -> int:
        # Initialize counter for valid subarrays
        count = 0

        # Iterate through all possible subarrays of length 3
        # For an array of length n, subarrays start from index 0 to n-3
        for i in range(len(nums) - 2):
            # Check condition: sum of first and third equals half of second
            # Use 2*(first + third) == second to avoid floating point issues
            if 2 * (nums[i] + nums[i + 2]) == nums[i + 1]:
                count += 1

        return count

    countSubarrays = count_subarrays
