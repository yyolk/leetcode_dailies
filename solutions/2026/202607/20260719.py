# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


class Solution:
    """1081. Smallest Subsequence of Distinct Characters

    Given a string s, return the lexicographically smallest subsequence of s
    that contains all the distinct characters of s exactly once.

    Constraints:
    * 1 <= s.length <= 1000
    * s consists of lowercase English letters.
    """

    def smallest_subsequence(self, s: str) -> str:
        # Record the last occurrence index of each character
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            # Skip if already included in the result subsequence
            if c in seen:
                continue
            # Pop larger characters that still appear later
            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.remove(stack.pop())
            # Include the current character
            stack.append(c)
            seen.add(c)
        return "".join(stack)

    smallestSubsequence = smallest_subsequence
