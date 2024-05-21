# https://leetcode.com/problems/sum-of-all-subset-xor-totals/


class Solution:
    """1863. Sum of All Subset XOR Totals

    The **XOR total** of an array is defined as the bitwise `XOR` of **all its
    elements**, or `0` if the array is **empty**.

    * For example, the **XOR total** of the array `[2,5,6]` is `2 XOR 5 XOR 6 = 1`.

    Given an array `nums`, return *the **sum** of all **XOR totals** for every
    **subset** of* `nums`.

    **Note:** Subsets with the **same** elements should be counted **multiple** times.

    An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by
    deleting some (possibly zero) elements of `b`.

    """

    def subset_x_o_r_sum(self, nums: list[int]) -> int:
        def dfs(index, current_xor):
            # Base case: If we've considered all elements
            if index == len(nums):
                return current_xor

            # Calculate the sum of XOR totals by including the current element
            include = dfs(index + 1, current_xor ^ nums[index])

            # Calculate the sum of XOR totals by excluding the current element
            exclude = dfs(index + 1, current_xor)

            # Return the sum of both including and excluding the current element
            return include + exclude

        # Start the recursion from index 0 with an initial XOR of 0
        return dfs(0, 0)

    subsetXORSum = subset_x_o_r_sum
