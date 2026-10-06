# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    """921. Minimum Add to Make Parentheses Valid

    A parentheses string is valid if and only if:

    * It is the empty string,
    * It can be written as AB (A concatenated with B), where A and B
      are valid strings, or
    * It can be written as (A), where A is a valid string.

    You are given a parentheses string s. In one move, you can insert a
    parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to
    be "(()))" or a closing parenthesis to be "())))".

    Return the minimum number of moves required to make s valid.

    Constraints:

    * 1 <= s.length <= 1000
    * s[i] is either '(' or ')'.
    """

    def min_add_to_make_valid(self, s: str) -> int:
        # Closers with no open match must be prefixed; leftover opens need a closer.
        unmatched_close = 0
        open_balance = 0
        for ch in s:
            if ch == "(":
                open_balance += 1
            elif open_balance:
                open_balance -= 1
            else:
                unmatched_close += 1
        return unmatched_close + open_balance

    minAddToMakeValid = min_add_to_make_valid
