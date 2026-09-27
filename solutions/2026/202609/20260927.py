# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/


class Solution:
    """1190. Reverse Substrings Between Each Pair of Parentheses

    You are given a string `s` that consists of lower case English letters and
    brackets.

    Reverse the strings in each pair of matching parentheses, starting from the
    innermost one.

    Your result should **not** contain any brackets.

    Constraints:

    * `1 <= s.length <= 2000`

    * `s` only contains lower case English characters and parentheses.

    * It is guaranteed that all parentheses are balanced.
    """

    def reverse_parentheses(self, s: str) -> str:
        """Reverse each parenthesized segment from the inside out."""
        stack: list[str] = []
        for ch in s:
            if ch != ")":
                stack.append(ch)
                continue
            # Pop the innermost segment until its matching '('.
            segment: list[str] = []
            while stack and stack[-1] != "(":
                segment.append(stack.pop())
            if stack:
                stack.pop()  # discard the matching '(' 
            # segment is already reversed by the pops; push it back.
            stack.extend(segment)
        return "".join(stack)

    reverseParentheses = reverse_parentheses
