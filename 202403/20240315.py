# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    """238. Product of Array Except Self

    Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]`
    *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

    The product of any prefix or suffix of `nums` is **guaranteed** to fit in a
    **32-bit** integer.

    You must write an algorithm that runs in `O(n)` time and without using the division
    operation.

    """

    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        # Calculate products of elements to the left of each element
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]

        # Calculate products of elements to the right of each element and update result
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result

    productExceptSelf = product_except_self
