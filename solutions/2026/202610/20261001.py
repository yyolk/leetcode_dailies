# https://leetcode.com/problems/valid-parentheses/


class Solution:
    """20. Valid Parentheses

    Given a string `s` containing just the characters `'('`, `')'`, `'{'`,
    `'}'`, `'['` and `']'`, determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.

    2. Open brackets must be closed in the correct order.

    3. Every close bracket has a corresponding open bracket of the same type.

    Constraints:

    * `1 <= s.length <= 104`

    * `s` consists of parentheses only `'()[]{}'`.
    """

    def is_valid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []
        for ch in s:
            if ch in pairs:
                # Closer must match the most recent unmatched opener.
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack

    isValid = is_valid
