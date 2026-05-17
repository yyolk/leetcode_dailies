# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/


class Solution:
    """1913. Maximum Product Difference Between Two Pairs

    The **product difference** between two pairs `(a, b)` and `(c, d)` is defined as `(a
    * b) - (c * d)`.

    * For example, the product difference between `(5, 6)` and `(2, 7)` is `(5 * 6) - (2
    * 7) = 16`.

    Given an integer array `nums`, choose four **distinct** indices `w`, `x`, `y`, and
    `z` such that the **product difference** between pairs `(nums[w], nums[x])` and
    `(nums[y], nums[z])` is **maximized**.

    Return *the **maximum** such product difference*.
    """

    def max_product_difference(self, nums: list[int]) -> int:
        # Sort the array in ascending order.
        nums.sort()

        # Calculate the product differences for the two pairs with the largest and
        # smallest values.
        max_product_difference = (nums[-1] * nums[-2]) - (nums[0] * nums[1])

        return max_product_difference

    maxProductDifference = max_product_difference
