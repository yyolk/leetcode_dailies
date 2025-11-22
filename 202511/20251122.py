# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/


class Solution:
    """3190. Find Minimum Operations to Make All Elements Divisible by Three

    You are given an integer array nums. In one operation, you can add or
    subtract 1 from any element of nums.

    Return the minimum number of operations to make every array element
    divisible by 3.

    Example: [1,2,3,4] -> 2  (1->0 or 2, 4->3 or 5)
    """
    def minimum_operations(self, nums: list[int]) -> int:
        total = 0
        for x in nums:
            # Compute remainder when divided by 3
            r = x % 3
            # If r == 0, no operation needed
            # If r == 1 or 2, one operation suffices (subtract or add 1)
            total += min(r, 3 - r)
        return total

    minimumOperations = minimum_operations