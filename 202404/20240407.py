# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    """678. Valid Parenthesis String

    Given a string `s` containing only three types of characters: `'('`, `')'` and
    `'*'`, return `true` *if* `s` *is **valid***.

    The following rules define a **valid** string:

    * Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.

    * Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.

    * Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.

    * `'*'` could be treated as a single right parenthesis `')'` or a single left
    parenthesis `'('` or an empty string `""`.

    """

    def check_valid_string(self, s: str) -> bool:
        # Stacks to keep track of indices of left parentheses and asterisks
        left_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == "(":
                left_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            else:  # char == ')'
                # Pop from left_stack if a matching left parenthesis is found
                if left_stack:
                    left_stack.pop()
                # If no matching left parenthesis, use an asterisk as one
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        # Match remaining left parentheses with asterisks if possible
        while left_stack and star_stack:
            if left_stack[-1] < star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                break

        # If all left parentheses are matched, the string is valid
        return not left_stack

    checkValidString = check_valid_string
