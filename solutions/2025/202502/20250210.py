# https://leetcode.com/problems/clear-digits/


class Solution:
    """3174. Clear Digits

    You are given a string `s`.

    Your task is to remove **all** digits by doing this operation repeatedly:

    * Delete the *first* digit and the **closest** **non-digit** character to its
    *left*.

    Return the resulting string after removing all digits."""

    def clear_digits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                # If the current character is a digit, pop the closest non-digit to its left
                if stack:
                    # Remove the closest non-digit to the left
                    stack.pop()
            else:
                # If it's not a digit, push it onto the stack
                stack.append(char)
        return "".join(stack)

    clearDigits = clear_digits
