# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    """713. Subarray Product Less Than K

    Given an array of integers `nums` and an integer `k`, return *the number of
    contiguous subarrays where the product of all the elements in the subarray is
    strictly less than* `k`.

    """

    def num_subarray_product_less_than_k(self, nums: list[int], k: int) -> int:
        # If k is less than or equal to 1, there are no valid subarrays
        if k <= 1:
            return 0
        
        # Initialize product and left pointer
        product = 1
        left = 0
        result = 0
        
        # Iterate through the array
        for right, num in enumerate(nums):
            # Update the product with the current number
            product *= num
            
            # If the product exceeds k, shrink the window
            while product >= k:
                # Update the product by removing the leftmost element
                product /= nums[left]
                # Move the left pointer to the right
                left += 1
                
            # Increment the result by the size of the current subarray
            result += right - left + 1
            
        # Return the total number of subarrays
        return result

    numSubarrayProductLessThanK = num_subarray_product_less_than_k
