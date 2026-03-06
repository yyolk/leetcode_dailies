# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones

class Solution:
    """1784. Check if Binary String Has at Most One Segment of Ones
    
    Given a binary string s without leading zeros, return true if s contains
    at most one contiguous segment of ones. Otherwise, return false.
    """
    def check_ones_segment(self, s: str) -> bool:
        # Once we see a 0 after some 1s, any later 1 means a second segment
        seen_zero = False
        
        for char in s:
            if char == "0":
                seen_zero = True
            # After seeing a 0, no more 1s are allowed
            elif seen_zero:
                return False
                
        return True

    checkOnesSegment = check_ones_segment