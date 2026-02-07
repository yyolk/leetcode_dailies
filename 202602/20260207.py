# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

class Solution:
    """1653. Minimum Deletions to Make String Balanced
    
    You are given a string s consisting only of characters 'a' and 'b'.
    
    You can delete any number of characters in s to make s balanced.
    
    s is balanced if there is no pair of indices (i,j) such that i < j
    
    and s[i] = 'b' and s[j] = 'a'.
    
    Return the minimum number of deletions needed to make s balanced.
    """
    def minimum_deletions(self, s: str) -> int:
        # Current minimum deletions to balance the prefix processed so far
        deletions = 0
        # Count of 'b's seen so far (potential trailing 'b's we may keep)
        b_count = 0
        
        for c in s:
            if c == "b":
                # Tentatively keep this 'b' - it extends the possible trailing 'b's
                b_count += 1
            else:
                # For 'a': choose cheaper option
                # - delete this 'a' (+1 deletion)
                # - or delete all previously counted 'b's to keep this 'a'
                deletions = min(deletions + 1, b_count)
        
        return deletions

    minimumDeletions = minimum_deletions