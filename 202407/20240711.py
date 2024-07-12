# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/


class Solution:
    """1190. Reverse Substrings Between Each Pair of Parentheses

    You are given a string `s` that consists of lower case English letters and brackets.

    Reverse the strings in each pair of matching parentheses, starting from the
    innermost one.

    Your result should **not** contain any brackets.

    """

    def reverse_parentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ")":
                # When encountering a closing parenthesis, start reversing
                substr = []
                while stack and stack[-1] != "(":
                    substr.append(stack.pop())
                # Pop the opening parenthesis "("
                stack.pop()
                # Add the reversed substring back to the stack
                stack.extend(substr)
            else:
                stack.append(char)

        # Join the characters in the stack to form the result
        return "".join(stack)

    reverseParentheses = reverse_parentheses
