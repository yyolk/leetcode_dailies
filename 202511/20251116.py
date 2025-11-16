# https://leetcode.com/problems/number-of-substrings-with-only-1s/


"""1513. Number of Substrings With Only 1s

Given a binary string s, return the number of substrings with all characters
1's. Since the answer may be too large, return it modulo 109 + 7.
"""


class Solution:
    def num_sub(self, s: str) -> int:
        # Modulo constant as per problem requirement
        MOD = 10**9 + 7
        # Accumulator for total substrings
        total = 0
        # Counter for current streak of '1's
        current = 0
        # Iterate through each character in the string
        for char in s:
            if char == "1":
                # Increment streak if '1'
                current += 1
            else:
                # Add substrings from current streak: n(n+1)/2 formula
                total += current * (current + 1) // 2
                # Apply modulo to prevent overflow
                total %= MOD
                # Reset streak on '0'
                current = 0
        # Add substrings from any remaining streak after loop
        total += current * (current + 1) // 2
        # Final modulo application
        total %= MOD
        return total

    numSub = num_sub
