# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


class Solution:
    """1614. Maximum Nesting Depth of the Parentheses

    Given a **valid parentheses string** `s`, return the **nesting depth** of
    `s`. The nesting depth is the **maximum** number of nested parentheses.

    Constraints:

    * `1 <= s.length <= 100`

    * `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`,
    `'('`, and `')'`.

    * It is guaranteed that parentheses expression `s` is a VPS.
    """

    def max_depth(self, s: str) -> int:
        """Return the maximum parenthesis nesting depth of VPS `s`."""
        depth = 0
        best = 0
        for ch in s:
            if ch == "(":
                # Depth increases only on an opening parenthesis.
                depth += 1
                if depth > best:
                    best = depth
            elif ch == ")":
                depth -= 1
        return best

    maxDepth = max_depth
