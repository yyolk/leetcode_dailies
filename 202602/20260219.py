# https://leetcode.com/problems/count-binary-substrings


class Solution:
    """696. Count Binary Substrings
    
    Given a binary string s, return the number of non-empty substrings
    that have the same number of 0's and 1's, and all the 0's and all
    the 1's in these substrings are grouped consecutively.
    
    Substrings that occur multiple times are counted the number of
    times they occur.
    """
    def count_binary_substrings(self, s: str) -> int:
        n = len(s)
        # Initialize answer and previous group length
        ans = 0
        prev = 0
        # Traverse the string
        i = 0
        while i < n:
            # Count the length of current group
            curr = 0
            char = s[i]
            while i < n and s[i] == char:
                curr += 1
                i += 1
            # Add the number of valid substrings from this and previous group
            ans += min(prev, curr)
            # Update previous group length
            prev = curr
        return ans

    countBinarySubstrings = count_binary_substrings