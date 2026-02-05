# https://leetcode.com/problems/transformed-array


class Solution:
    """3379. Transformed Array
    
    You are given an integer array nums that represents a circular array.
    Create a new array result of the same size.
    
    For each index i (0 <= i < len(nums)):
    - If nums[i] > 0: move nums[i] steps right circularly from i.
      Set result[i] to nums[landing index].
    - If nums[i] < 0: move abs(nums[i]) steps left circularly from i.
      Set result[i] to nums[landing index].
    - If nums[i] == 0: set result[i] = nums[i].
    
    Return result.
    
    Note: The array is circular; indices wrap around the ends.
    """
    def construct_transformed_array(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            # Landing index: i + nums[i] steps, modulo n.
            # Python's % operator handles negative nums[i] correctly
            # (negative remainder becomes positive).
            target = (i + nums[i]) % n
            result[i] = nums[target]
        return result

    constructTransformedArray = construct_transformed_array