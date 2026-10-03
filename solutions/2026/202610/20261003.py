# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    """32. Longest Valid Parentheses

    Given a string containing just the characters '(' and ')', return the
    length of the longest valid (well-formed) parentheses substring.

    Constraints:

    * 0 <= s.length <= 3 * 10^4
    * s[i] is '(' or ')'.
    """

    def longest_valid_parentheses(self, s: str) -> int:
        best = 0
        # Left-to-right catches valid spans that close before extra openers.
        opens = 0
        closes = 0
        for char in s:
            if char == "(":
                opens += 1
            else:
                closes += 1
            if closes == opens:
                best = max(best, opens + closes)
            elif closes > opens:
                # Extra closer cannot extend any earlier valid substring.
                opens = 0
                closes = 0
        # Right-to-left catches spans that open after extra closers, e.g. "(()".
        opens = 0
        closes = 0
        for char in reversed(s):
            if char == "(":
                opens += 1
            else:
                closes += 1
            if opens == closes:
                best = max(best, opens + closes)
            elif opens > closes:
                opens = 0
                closes = 0
        return best

    longestValidParentheses = longest_valid_parentheses
