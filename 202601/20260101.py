# https://leetcode.com/problems/plus-one


class Solution:
    """66. Plus One

    You are given a large integer represented as an integer array `digits`,
    where each `digits[i]` is the ith digit of the integer. The digits are
    ordered from most significant to least significant. The integer has no
    leading zeros.

    Increment the large integer by one and return the resulting array of
    digits.
    """
    def plus_one(self, digits: list[int]) -> list[int]:
        # Start from the least significant digit
        i = len(digits) - 1
        
        # Propagate the carry from right to left
        while i >= 0:
            # Add 1 to current digit (only first iteration effectively adds 1)
            digits[i] += 1
            
            # If no overflow (digit < 10), carry is done
            if digits[i] < 10:
                return digits
            
            # Overflow: set current digit to 0 and continue carry
            digits[i] = 0
            i -= 1
        
        # If we reach here, there was a carry out of the most significant digit
        # (e.g., 999 -> 1000), so insert a new leading 1
        return [1] + digits

    plusOne = plus_one