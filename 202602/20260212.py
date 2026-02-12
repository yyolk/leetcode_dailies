# https://leetcode.com/problems/longest-balanced-substring-i

class Solution:
    """3713. Longest Balanced Substring I
    
    You are given a string s consisting of lowercase English letters.
    A substring of s is called balanced if all distinct characters in the
    substring appear the same number of times.
    
    Return the length of the longest balanced substring of s.
    """
    def longest_balanced(self, s: str) -> int:
        n = len(s)
        max_length = 0
        offset = ord("a")
        
        for start in range(n):
            # Remaining length cannot exceed current max_length; skip rest
            if n - start <= max_length:
                break
            
            freq = [0] * 26
            
            for end in range(start, n):
                # Increment frequency for the character at end
                freq[ord(s[end]) - offset] += 1
                
                # Compute min and max among frequencies > 0
                min_freq = float("inf")
                max_freq = 0
                for f in freq:
                    if f > 0:
                        min_freq = min(min_freq, f)
                        max_freq = max(max_freq, f)
                
                # If all positive frequencies are equal, update answer
                if min_freq == max_freq:
                    max_length = max(max_length, end - start + 1)
        
        return max_length

    longestBalanced = longest_balanced