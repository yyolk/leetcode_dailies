# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/


class Solution:
    """1541. Minimum Insertions to Balance a Parentheses String

    Given a parentheses string `s` containing only the characters `'('` and `')'`. A
    parentheses string is **balanced** if:

    * Any left parenthesis `'('` must have a corresponding two consecutive right
    parenthesis `'))'`.

    * Left parenthesis `'('` must go before the corresponding two consecutive right
    parenthesis `'))'`.

    In other words, we treat `'('` as an opening parenthesis and `'))'` as a closing
    parenthesis.

    * For example, `"())"`, `"())(())))"` and `"(())())))"` are balanced, `")()"`,
    `"()))"` and `"(()))"` are not balanced.

    You can insert the characters `'('` and `')'` at any position of the string to
    balance it if needed.

    Return *the minimum number of insertions* needed to make `s` balanced.

    Constraints:

    * `1 <= s.length <= 105`

    * `s` consists of `'('` and `')'` only."""

    def min_insertions(self, s: str) -> int:
        """...

        Proposed solution ...

        Args:
            s (str): ...

        Returns:
            int: ..."""
        ...

    minInsertions = min_insertions
