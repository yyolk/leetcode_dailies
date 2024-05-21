# https://leetcode.com/problems/subsets/


class Solution:
    """78. Subsets

    Given an integer array `nums` of **unique** elements, return *all possible*
    *subsets* *(the power set)*.

    The solution set **must not** contain duplicate subsets. Return the solution in
    **any order**.

    """

    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int, current_subset: list[int]):
            # Append a copy of the current subset to the result
            result.append(current_subset[:])
            # Iterate through the remaining elements
            for i in range(start, len(nums)):
                # Include the current element and move to the next
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                # Exclude the current element and backtrack
                current_subset.pop()
        
        result = []
        backtrack(0, [])
        return result