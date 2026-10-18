# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/


class Solution:
    """1569. Number of Ways to Reorder Array to Get Same BST

    Given an array nums that represents a permutation of integers from 1 to n.
    We are going to construct a binary search tree (BST) by inserting the
    elements of nums in order into an initially empty BST. Find the number of
    different ways to reorder nums so that the constructed BST is identical to
    that formed from the original array nums.

    For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left
    child, and 3 as a right child. The array [2,3,1] also yields the same BST
    but [3,2,1] yields a different BST.

    Return the number of ways to reorder nums such that the BST formed is
    identical to the original BST formed from nums.

    Since the answer may be very large, return it modulo 10**9 + 7.

    Constraints:

    * 1 <= nums.length <= 1000

    * 1 <= nums[i] <= nums.length

    * All integers in nums are distinct.
    """

    def num_of_ways(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # Precompute binomial coefficients C[i][j] = C(i, j) mod MOD.
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def dfs(arr: list[int]) -> int:
            # Base: 0, 1, or 2 elements have only one ordering.
            if len(arr) <= 2:
                return 1
            root = arr[0]
            # Partition remaining elements into left and right subtrees.
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            # Ways to interleave left and right while preserving relative order.
            ways = comb[len(left) + len(right)][len(left)]
            return ways * dfs(left) * dfs(right) % MOD

        # Total valid orderings including the original; subtract 1.
        return (dfs(nums) - 1) % MOD

    numOfWays = num_of_ways
