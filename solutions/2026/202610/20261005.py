# https://leetcode.com/problems/score-of-parentheses/


class Solution:
    """856. Score of Parentheses

    Given a balanced parentheses string s, return the score of the string.

    The score of a balanced parentheses string is based on the following rule:

    * "()" has score 1.
    * AB has score A + B, where A and B are balanced parentheses strings.
    * (A) has score 2 * A, where A is a balanced parentheses string.

    Constraints:

    * 2 <= s.length <= 50
    * s consists of only '(' and ')'.
    * s is a balanced parentheses string.
    """

    def score_of_parentheses(self, s: str) -> int:
        score = 0
        depth = 0
        for i, char in enumerate(s):
            if char == "(":
                depth += 1
                continue
            depth -= 1
            # Only a primitive "()" contributes; nesting multiplies by 2^depth.
            if s[i - 1] == "(":
                score += 1 << depth
        return score

    scoreOfParentheses = score_of_parentheses
