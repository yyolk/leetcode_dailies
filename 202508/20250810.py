# https://leetcode.com/problems/reordered-power-of-2/


class Solution:
    """869. Reordered Power of 2

    You are given an integer `n`. We reorder the digits in any order (including the
    original order) such that the leading digit is not zero.

    Return `true` *if and only if we can do this so that the resulting number is a power
    of two*."""

    def reordered_power_of2(self, n: int) -> bool:
        # Sort the digits of n in ascending order to create a canonical representation
        s = "".join(sorted(str(n)))
        # Determine the number of digits in n
        len_n = len(s)
        # Initialize the power of 2 value starting from 2^0 = 1
        pow_val = 1
        # Initialize the exponent for powers of 2
        i = 0
        # Continue looping while the power of 2 has fewer or equal digits than n
        while pow_val < 10**len_n:
            # Convert the current power of 2 to a string
            pow_str = str(pow_val)
            # Check if the power has the same number of digits and matches the sorted digits of n
            if len(pow_str) == len_n and "".join(sorted(pow_str)) == s:
                return True
            # Increment the exponent
            i += 1
            # Calculate the next power of 2 using bit shift
            pow_val = 1 << i
        # If no matching power of 2 is found, return False
        return False

    reorderedPowerOf2 = reordered_power_of2
