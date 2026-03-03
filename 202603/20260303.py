# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string

class Solution:
    """1545. Find Kth Bit in Nth Binary String
    
    Given two positive integers n and k, the binary string Sn is formed as
    follows:
    
    S1 = "0"
    
    Si = S(i-1) + "1" + reverse(invert(S(i-1))) for i > 1
    
    Where + denotes the concatenation operation, reverse(x) returns the
    reversed string x, and invert(x) inverts all the bits in x (0 changes to 1
    and 1 changes to 0).
    
    Return the kth bit in Sn. It is guaranteed that k is valid for the given
    n.
    """
    def find_kth_bit(self, n: int, k: int) -> str:
        # Iterative descent: O(n) time, O(1) space
        # n<=20 so loop is fast
        flip = 0
        while n > 1:
            # mid is position of the central '1'
            mid = 1 << (n - 1)
            if k == mid:
                # '1' with accumulated flips
                return str(1 ^ flip)
            if k > mid:
                # reflect position across middle and invert
                k = 2 * mid - k
                flip ^= 1
            n -= 1
        # S1 base case "0" with flips
        return str(flip)

    findKthBit = find_kth_bit