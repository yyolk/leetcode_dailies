# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

class Solution:
    """1758. Minimum Changes To Make Alternating Binary String
    
    You are given a string s of '0's and '1's.
    In one operation, change any '0' to '1' or '1' to '0'.
    Return the minimum operations needed to make s alternating
    (no two adjacent characters are equal).
    """
    def min_operations(self, s: str) -> int:
        # Count changes needed if we start with '0'
        count_start_zero = 0
        for i, char in enumerate(s):
            # For even indices expect '0', odd expect '1'
            expected = '0' if i % 2 == 0 else '1'
            if char != expected:
                count_start_zero += 1
        
        # Count changes needed if we start with '1'
        count_start_one = 0
        for i, char in enumerate(s):
            # For even indices expect '1', odd expect '0'
            expected = '1' if i % 2 == 0 else '0'
            if char != expected:
                count_start_one += 1
        
        # The minimum of the two possible patterns is the answer
        return min(count_start_zero, count_start_one)

    minOperations = min_operations