# https://leetcode.com/problems/binary-gap


class Solution:
    """868. Binary Gap
    
    Given a positive integer n, find and return the longest distance between
    any two adjacent 1's in the binary representation of n. If there are no
    two adjacent 1's, return 0.
    
    Two 1's are adjacent if there are only 0's separating them (possibly no
    0's). The distance between two 1's is the absolute difference between
    their bit positions. For example, the two 1's in "1001" have a distance
    of 3.
    """
    def binary_gap(self, n: int) -> int:
        max_dist = 0
        # Position of previous 1 (invalid initially)
        prev = -1
        # Current bit position from LSB
        pos = 0
        while n > 0:
            if n & 1:  # Current bit is 1
                if prev != -1:
                    # Distance is position diff (includes intervening 0s)
                    max_dist = max(max_dist, pos - prev)
                prev = pos  # Update previous
            n >>= 1  # Check next bit
            pos += 1
        return max_dist

    binaryGap = binary_gap