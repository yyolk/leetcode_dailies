# https://leetcode.com/problems/generate-parentheses/


class Solution:
    """22. Generate Parentheses

    Given n pairs of parentheses, write a function to generate all
    combinations of well-formed parentheses.

    Constraints:

    * 1 <= n <= 8
    """

    def generate_parenthesis(self, n: int) -> list[str]:
        result: list[str] = []
        # Reuse one buffer; each complete string is copied into result.
        path = ["("] * (2 * n)

        def build(open_count: int, close_count: int, index: int) -> None:
            if index == 2 * n:
                result.append("".join(path))
                return
            # An opener is valid while fewer than n have been placed.
            if open_count < n:
                path[index] = "("
                build(open_count + 1, close_count, index + 1)
            # A closer is valid only when it will not outnumber openers.
            if close_count < open_count:
                path[index] = ")"
                build(open_count, close_count + 1, index + 1)

        # Every well-formed string starts with an opener.
        build(1, 0, 1)
        return result

    generateParenthesis = generate_parenthesis
