# https://leetcode.com/problems/smallest-number-with-all-set-bits/


class Solution:
    """3370. Smallest Number With All Set Bits

    You are given a *positive* number `n`.

    Return the **smallest** number `x` **greater than** or **equal to** `n`, such that
    the binary representation of `x` contains only set bits"""

    def smallest_number(self, n: int) -> int:
        # Compute the target for the next power of 2
        m = n + 1
        # Determine the bit length of m
        bit_len = m.bit_length()
        # Calculate the highest power of 2 less than or equal to m
        high_bit = 1 << (bit_len - 1)
        # If m is exactly a power of 2, use it; otherwise, shift to the next power
        if high_bit == m:
            power = high_bit
        else:
            power = high_bit << 1
        # The result is one less than the power of 2, ensuring all bits set
        return power - 1

    smallestNumber = smallest_number
