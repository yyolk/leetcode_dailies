# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution:
    """3300. Minimum Element After Replacement With Digit Sum

    You are given an integer array nums. You replace each element in nums with
    the sum of its digits. Return the minimum element in nums after all
    replacements.
    """
    def min_element(self, nums: list[int]) -> int:
        # Track the smallest digit sum encountered
        min_sum = float("inf")
        for num in nums:
            # Sum digits of current num using modulo and division
            digit_sum = 0
            current = num
            while current > 0:
                # Add last digit to sum
                digit_sum += current % 10
                # Remove last digit
                current //= 10
            # Update minimum sum found so far
            min_sum = min(min_sum, digit_sum)
        return min_sum

    minElement = min_element