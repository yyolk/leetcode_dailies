# https://leetcode.com/problems/keep-multiplying-found-values-by-two/


class Solution:
    """2154. Keep Multiplying Found Values by Two

    You are given an array of integers nums. You are also given an integer
    original which is the first number that needs to be searched for in nums.

    You then do the following steps:

    If original is found in nums, multiply it by two (i.e., set original = 2 *
    original).
    Otherwise, stop the process.
    Repeat this process with the new number as long as you keep finding the
    number.
    Return the final value of original.
    """
    def find_final_value(self, nums: list[int], original: int) -> int:
        # Convert nums to set for O(1) average-case lookups
        seen = set(nums)
        
        # Keep doubling original while it exists in the set
        while original in seen:
            original *= 2
            
        return original

    findFinalValue = find_final_value