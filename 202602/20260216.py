# https://leetcode.com/problems/reverse-bits


class Solution:
    """190. Reverse Bits
    
    Reverse the bits of a given 32-bit unsigned integer.
    """

    def reverse_bits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            # Shift accumulated result left to make room for next bit
            # OR with current LSB of n (adds the bit as new LSB)
            result = (result << 1) | (n & 1)
            # Move to next bit in n
            n >>= 1
        
        return result

    reverseBits = reverse_bits