# https://leetcode.com/problems/maximum-odd-binary-number/


class Solution:
    """2864. Maximum Odd Binary Number

    You are given a **binary** string `s` that contains at least one `'1'`.

    You have to **rearrange** the bits in such a way that the resulting binary number is
    the **maximum odd binary number** that can be created from this combination.

    Return *a string representing the maximum odd binary number that can be created from
    the given combination.*

    **Note** that the resulting string **can** have leading zeros.

    """

    def maximum_odd_binary_number(self, s: str) -> str:
        # List to store '1's encountered in the string
        ones = []
        
        # String to store the remaining '0's and '1's
        remaining = ""

        # Iterate through each character in the input string
        for c in s:
            if c == "1":
                # If the character is '1', add it to the 'ones' list
                ones.append(c)
            else:
                # If the character is '0', add it to the 'remaining' string
                remaining += c
        
        # Move the rightmost '1' to the beginning of the string
        remaining += ones.pop()

        # Reconstruct the remaining string by adding '1's back in their original order
        for one in ones:
            remaining = one + remaining
        
        # Return the resulting maximum odd binary number
        return remaining

    maximumOddBinaryNumber = maximum_odd_binary_number
