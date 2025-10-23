# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/


class Solution:
    """3461. Check If Digits Are Equal in String After Operations I

    You are given a string `s` consisting of digits. Perform the following operation
    repeatedly until the string has **exactly** two digits:

    * For each pair of consecutive digits in `s`, starting from the first digit,
    calculate a new digit as the sum of the two digits **modulo** 10.

    * Replace `s` with the sequence of newly calculated digits, *maintaining the order*
    in which they are computed.

    Return `true` if the final two digits in `s` are the **same**; otherwise, return
    `false`."""

    def has_same_digits(self, s: str) -> bool:
        # Convert the input string to a list of integers for easier summation and modulo operations
        digits = [int(c) for c in s]
        
        # Continue the process until the list is reduced to exactly two digits
        while len(digits) > 2:
            # Initialize an empty list to hold the new digits after the current operation
            new_digits = []
            
            # Iterate over consecutive pairs, compute their sum modulo 10, and append to new list
            for i in range(len(digits) - 1):
                # Sum the current and next digit, then take modulo 10 to get the new digit
                sum_mod = (digits[i] + digits[i + 1]) % 10
                new_digits.append(sum_mod)
            
            # Replace the current digits list with the newly computed one
            digits = new_digits
        
        # After reduction, check if the two remaining digits are equal
        return digits[0] == digits[1]

    hasSameDigits = has_same_digits
