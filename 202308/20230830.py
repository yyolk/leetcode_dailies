# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """2366. Minimum Replacements to Sort the Array

        You are given a **0-indexed** integer array `nums`.
        In one operation you can replace any element of the array with **any two**
        elements that **sum** to it.

        For example, consider `nums = [5,6,7]`.
        In one operation, we can replace `nums[1]` with `2` and `4` and
        convert `nums` to `[5,2,4,7]`.
        Return the _minimum number of operations to make an array that is sorted
        in **non-decreasing** order_.

        Args:
            nums (List of int): The input array with numbers to be reduced

        Returns:
            int: The minimum number of operations to make the input that is sorted in non-decreasing order
        """
        operations = 0
        n = len(nums)

        # Initialize prev_value with the last element of the array
        prev_value = nums[n - 1]

        # Iterate through the array in reverse order (from second-to-last element to the first)
        for i in range(n - 2, -1, -1):
            if nums[i] > prev_value:
                # Calculate how many times prev_value needs to be summed to exceed nums[i]
                k = (nums[i] + prev_value - 1) // prev_value

                # Increment operations by k - 1 (since k - 1 replacements are needed)
                operations += k - 1

                # Update prev_value to the floor division of nums[i] by k
                prev_value = nums[i] // k
            else:
                # If nums[i] is not greater than prev_value, update prev_value to nums[i]
                prev_value = nums[i]

        return operations
