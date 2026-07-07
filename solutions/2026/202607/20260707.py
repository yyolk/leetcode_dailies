# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/


class Solution:
    """3754. Concatenate Non-Zero Digits and Multiply by Sum I

    You are given an integer n. Form a new integer x by concatenating all the
    non-zero digits of n in their original order. If there are no non-zero
    digits, x = 0. Let sum be the sum of digits in x. Return an integer
    representing the value of x * sum.
    Constraints: 0 <= n <= 10**9"""

    def sum_and_multiply(self, n: int) -> int:
        x = 0
        digit_sum = 0
        # Process digits from left to right (original order)
        for c in str(n):
            if c != "0":
                d = int(c)
                # Shift x left (multiply by 10) and append the digit
                x = x * 10 + d
                # Add to sum (digits of x are exactly these non-zero digits)
                digit_sum += d
        # For n=0 or all zeros: x=0, digit_sum=0 so product=0
        return x * digit_sum

    sumAndMultiply = sum_and_multiply
