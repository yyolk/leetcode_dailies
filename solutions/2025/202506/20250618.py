# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/


class Solution:
    """2966. Divide Array Into Arrays With Max Difference

    You are given an integer array `nums` of size `n` where `n` is a multiple of 3 and a
    positive integer `k`.

    Divide the array `nums` into `n / 3` arrays of size **3** satisfying the following
    condition:

    * The difference between **any** two elements in one array is **less than or equal**
    to `k`.

    Return a **2D** array containing the arrays. If it is impossible to satisfy the
    conditions, return an empty array. And if there are multiple answers, return **any**
    of them."""

    def divide_array(self, nums: list[int], k: int) -> list[list[int]]:
        # Sort the array to bring elements that are close in value next to each other
        nums.sort()

        # Initialize the result list to store the subarrays
        result = []

        # Iterate through the array in steps of 3
        for i in range(0, len(nums), 3):
            # Check if the difference between max and min in the group exceeds k
            if nums[i + 2] - nums[i] > k:
                return []
            # If the condition is satisfied, append the group to the result
            result.append([nums[i], nums[i + 1], nums[i + 2]])

        # Return the list of subarrays if all groups satisfy the condition
        return result

    divideArray = divide_array
