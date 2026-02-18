# https://leetcode.com/problems/binary-number-with-alternating-bits


class Solution:
    """693. Binary Number with Alternating Bits
    
    Given a positive integer n, check whether it has alternating bits:
    namely, if two adjacent bits will always have different values.
    """
    def has_alternating_bits(self, n: int) -> bool:
        # Compare n with right-shifted version → adjacent bits differ
        # if (n ^ (n >> 1)) has no overlapping 1s with itself shifted
        x = n ^ (n >> 1)
        
        # A number with all 1s in binary is one less than a power of 2
        # Check if x+1 is power of 2 → means x had only consecutive 1s
        # For alternating pattern, x should be all 1s up to bit length
        return (x & (x + 1)) == 0

    hasAlternatingBits = has_alternating_bits