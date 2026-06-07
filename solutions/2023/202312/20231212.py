# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
import heapq


class Solution:
    """1464. Maximum Product of Two Elements in an Array

    Given the array of integers `nums`, you will choose two different indices `i` and
    `j` of that array. *Return the maximum value of* `(nums[i]-1)*(nums[j]-1)`.
    """

    def max_product(self, nums: list[int]) -> int:
        """Find the max product of any coupling of integers.

        Uses heapq.nlargest(...) to pick out the two largest integers.
        The indexes of i, j are not relevant for finding the solution.

        Args:
            nums: Input list of integers.

        Returns:
            The max product of the two largest integers.
        """
        num_i, num_j = heapq.nlargest(2, nums)
        return (num_i - 1) * (num_j - 1)

    maxProduct = max_product
