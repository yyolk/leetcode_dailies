# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/


class Solution:
    """2966. Divide Array Into Arrays With Max Difference

    You are given an integer array `nums` of size `n` and a positive integer `k`.

    Divide the array into one or more arrays of size `3` satisfying the following
    conditions:

    * **Each** element of `nums` should be in **exactly** one array.

    * The difference between **any** two elements in one array is less than or equal to
    `k`.

    Return *a* **2D** *array containing all the arrays. If it is impossible to satisfy
    the conditions, return an empty array. And if there are multiple answers, return
    **any** of them.*

    """

    def divide_array(self, nums: list[int], k: int) -> list[list[int]]:
        # Check if the size of nums is not divisible by 3
        size = len(nums)
        if size % 3 != 0:
            return []

        # Sort the array
        nums.sort()

        # Initialize an empty result list and a variable to track the group index
        result = []
        group_index = 0

        # Iterate through the array in steps of 3
        for i in range(0, size, 3):
            # Check if there are three elements in the current subarray
            if i + 2 < size and nums[i + 2] - nums[i] <= k:
                # Add the current subarray to the result
                result.append([nums[i], nums[i + 1], nums[i + 2]])
                group_index += 1
            else:
                # If the conditions are not met, return an empty array
                return []

        # Return the final result containing valid subarrays
        return result

    divideArray = divide_array
