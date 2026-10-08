# https://leetcode.com/problems/remove-outermost-parentheses/


class Solution:
    """1021. Remove Outermost Parentheses

    A valid parentheses string is either empty "", "(" + A + ")", or A + B,
    where A and B are valid parentheses strings, and + is concatenation.

    A valid parentheses string s is primitive if it is nonempty and cannot be
    split into s = A + B with A and B both nonempty valid parentheses strings.

    Given a valid parentheses string s, consider its primitive decomposition
    s = P1 + P2 + ... + Pk. Return s after removing the outermost parentheses
    of every primitive string in that decomposition.

    Constraints:

    * 1 <= s.length <= 10^5
    * s[i] is either '(' or ')'.
    * s is a valid parentheses string.
    """

    def remove_outer_parentheses(self, s: str) -> str:
        """Drop the outer parentheses of each primitive component."""
        parts: list[str] = []
        depth = 0
        for char in s:
            if char == "(":
                # Depth 0 marks the outer open of a primitive component.
                if depth > 0:
                    parts.append(char)
                depth += 1
            else:
                depth -= 1
                # Depth 0 marks the outer close; keep only inner closes.
                if depth > 0:
                    parts.append(char)
        return "".join(parts)

    removeOuterParentheses = remove_outer_parentheses
