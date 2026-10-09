# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/


class Solution:
    """1541. Minimum Insertions to Balance a Parentheses String

    Given a parentheses string s containing only '(' and ')'. A parentheses
    string is balanced if:

    * Any left parenthesis '(' must have a corresponding two consecutive right
      parenthesis '))'.
    * Left parenthesis '(' must go before the corresponding two consecutive
      right parenthesis '))'.

    In other words, treat '(' as an opening parenthesis and '))' as a closing
    parenthesis.

    For example, "())", "())(())))" and "(())())))" are balanced, ")()",
    "()))" and "(()))" are not balanced.

    Insert '(' and ')' at any position to balance s if needed.

    Return the minimum number of insertions needed to make s balanced.

    Constraints:

    * 1 <= s.length <= 10^5
    * s consists of '(' and ')' only.
    """

    def min_insertions(self, s: str) -> int:
        """Count the fewest inserts so each '(' is matched by '))'."""
        insertions = 0
        # Closing parens still required by unmatched openings.
        needed = 0
        for char in s:
            if char == "(":
                # A lone ')' leaves an odd close; pair it before a new open.
                if needed % 2:
                    insertions += 1
                    needed -= 1
                needed += 2
            else:
                needed -= 1
                if needed < 0:
                    # This ')' has no open; insert '(' and still need one ')'.
                    insertions += 1
                    needed = 1
        return insertions + needed

    minInsertions = min_insertions
