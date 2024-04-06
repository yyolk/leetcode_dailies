# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    """1249. Minimum Remove to Make Valid Parentheses

    Given a string s of `'('` , `')'` and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any
    positions ) so that the resulting *parentheses string* is valid and return **any**
    valid string.

    Formally, a *parentheses string* is valid if and only if:

    * It is the empty string, contains only lowercase characters, or

    * It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid
    strings, or

    * It can be written as `(A)`, where `A` is a valid string.

    """

    def min_remove_to_make_valid(self, s: str) -> str:
        # Convert the string to a list for easy modification
        s_list = list(s)
        stack = []

        # Iterate through the string to find invalid parentheses
        for i, char in enumerate(s_list):
            if char == "(":
                stack.append(i)
            elif char == ")":
                # If there's a matching '(' on the stack, remove it from the stack
                if stack:
                    stack.pop()
                else:
                    # If no matching '(' on the stack, mark this ')' for removal
                    s_list[i] = ""

        # Remove any unmatched '(' from the stack
        while stack:
            s_list[stack.pop()] = ""

        # Join the modified list back into a string and return it
        return "".join(s_list)

    minRemoveToMakeValid = min_remove_to_make_valid
