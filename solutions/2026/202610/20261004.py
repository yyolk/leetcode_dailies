# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    """678. Valid Parenthesis String

    Given a string s containing only '(', ')' and '*', return true if s is
    valid.

    A valid string pairs every '(' with a later ')'. '*' may be '(', ')', or
    an empty string.

    Constraints:

    * 1 <= s.length <= 100
    * s[i] is '(', ')' or '*'.
    """

    def check_valid_string(self, s: str) -> bool:
        low = 0
        high = 0
        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                low -= 1
                high -= 1
            else:
                # '*' can close one open, or open one more.
                low -= 1
                high += 1
            if high < 0:
                # More closes than any choice of '*' can cover.
                return False
            if low < 0:
                # Extra closes can be absorbed by treating '*' as empty.
                low = 0
        return low == 0

    checkValidString = check_valid_string
