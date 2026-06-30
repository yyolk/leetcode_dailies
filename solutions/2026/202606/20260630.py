# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    """1358. Number of Substrings Containing All Three Characters
    
    Given a string s consisting only of characters a, b and c. Return the number of
    substrings containing at least one occurrence of all these characters a, b and
    c.
    
    Constraints:
    * 3 <= s.length <= 5 x 10^4
    * s only consists of a, b or c characters."""
    def number_of_substrings(self, s: str) -> int:
        # last[0/1/2] = latest index of a/b/c
        last = [-1] * 3
        ans = 0
        for i, char in enumerate(s):
            # update latest for seen char
            last[ord(char) - ord("a")] = i
            # valid starts for end=i: 0..min(last) (adds 0 early)
            ans += min(last) + 1
        return ans

    numberOfSubstrings = number_of_substrings
