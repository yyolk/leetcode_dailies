# https://leetcode.com/problems/permutations/


class Solution:
    """46. Permutations

    Given an array `nums` of distinct integers, return *all the possible permutations*.
    You can return the answer in **any order**.

    """

    def permute(self, nums: list[int]) -> list[list[int]]:
        # Helper function for backtracking
        def backtrack(first):
            # If all elements are used, add the permutation to the output
            if first == n:
                output.append(nums[:])
            # Generate permutations recursively
            for i in range(first, n):
                # Swap elements to generate different permutations
                nums[first], nums[i] = nums[i], nums[first]
                # Recursively call backtrack for the next index
                backtrack(first + 1)
                # Undo the swap for backtracking
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        # Start backtracking from index 0
        backtrack(0)
        return output
