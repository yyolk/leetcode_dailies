# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    """1464. Maximum Product of Two Elements in an Array

    Given the array of integers `nums`, you will choose two different indices `i`
    and `j` of that array. *Return the maximum value of*
    `(nums[i]-1)*(nums[j]-1)`.
    Constraints:
    * `2 <= nums.length <= 500`
    * `1 <= nums[i] <= 10^3`
    """
    def max_product(self, nums: list[int]) -> int:
        # Initialize trackers for the two largest values
        max1 = max2 = 0
        for num in nums:
            # If current exceeds the largest, demote previous largest
            if num > max1:
                max2 = max1
                max1 = num
            # Else update second-largest if needed
            elif num > max2:
                max2 = num
        # Return the product after subtracting 1 from each
        return (max1 - 1) * (max2 - 1)

    maxProduct = max_product
