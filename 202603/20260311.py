# https://leetcode.com/problems/complement-of-base-10-integer

class Solution:
    """1009. Complement of Base 10 Integer
    
    The complement of an integer is the integer you get when you flip all the 0's 
    to 1's and all the 1's to 0's in its binary representation.
    
    For example, The integer 5 is "101" in binary and its complement is "010" 
    which is the integer 2.
    
    Given an integer n, return its complement.
    """
    def bitwise_complement(self, n: int) -> int:
        # Get bit length, default to 1 for n=0 edge case
        bit_length = n.bit_length() or 1
        # Mask is all 1s matching the bit length
        mask = (1 << bit_length) - 1
        # XOR flips bits in the binary representation
        return n ^ mask

    bitwiseComplement = bitwise_complement