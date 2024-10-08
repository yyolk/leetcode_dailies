# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


class Solution:
    """2696. Minimum String Length After Removing Substrings

    You are given a string `s` consisting only of **uppercase** English letters.

    You can apply some operations to this string where, in one operation, you can remove
    **any** occurrence of one of the substrings `"AB"` or `"CD"` from `s`.

    Return *the **minimum** possible length of the resulting string that you can
    obtain*.

    **Note** that the string concatenates after removing the substring and could produce
    new `"AB"` or `"CD"` substrings.

    """

    def min_length(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and (
                (char == "B" and stack[-1] == "A") or (char == "D" and stack[-1] == "C")
            ):
                # Remove the last character because it forms "AB" or "CD"
                stack.pop()
            else:
                # Add the character to the stack
                stack.append(char)

        return len(stack)

    minLength = min_length
