# https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution:
    """628. Maximum Product of Three Numbers

    Given an integer array nums, find three numbers whose product is
    maximum and return the maximum product.
    Constraints:
    * 3 <= nums.length <= 104
    * -1000 <= nums[i] <= 1000
    """

    def maximum_product(self, nums: list[int]) -> int:
        # Sort to easily access the smallest and largest values
        nums.sort()
        # Product of the three largest numbers
        product1 = nums[-1] * nums[-2] * nums[-3]
        # Product of the two smallest (possible negatives) and the largest
        product2 = nums[0] * nums[1] * nums[-1]
        # Return the larger of the two candidate products
        return max(product1, product2)

    maximumProduct = maximum_product
