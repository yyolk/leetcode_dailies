# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers
MOD = 10**9 + 7

class Solution:
    """1680. Concatenation of Consecutive Binary Numbers
    
    Given an integer n, return the decimal value of the binary string formed by
    concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.
    """
    def concatenated_binary(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            # bit length of i (exact bits in its binary rep, no leading zeros)
            bit_len = i.bit_length()
            # left shift appends the binary of i (equivalent to * 2**bit_len)
            # add i then mod to prevent overflow and keep within bounds
            result = ((result << bit_len) + i) % MOD
        return result

    concatenatedBinary = concatenated_binary