# https://leetcode.com/problems/permutation-in-string/


class Solution:
    """567. Permutation in String

    Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of
    `s1`, or `false` otherwise.

    In other words, return `true` if one of `s1`'s permutations is the substring of
    `s2`.

    """

    def check_inclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains any permutation of s1.
        
        Args:
        s1 (str): The string to find a permutation of.
        s2 (str): The string to search in.
        
        Returns:
        bool: True if s2 contains a permutation of s1, False otherwise.
        
        Time complexity: O(len(s2))
        Space complexity: O(1) because the size of the Counter is at most 26 for lowercase English letters.
        """
        # If s1 is longer than s2, no permutation can exist in s2
        if len(s1) > len(s2):
            return False
        
        # Create frequency counters for s1 and for the first window in s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        
        # Check if the first window is a permutation
        if s1_count == window_count:
            return True
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the character going out of the window scope
            window_count[s2[i - len(s1)]] -= 1
            # If the count goes to zero, remove the key for efficiency
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            
            # If current window matches the s1_count, we've found a permutation
            if window_count == s1_count:
                return True
        
        return False

    checkInclusion = check_inclusion
