# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    """921. Minimum Add to Make Parentheses Valid

    A parentheses string is valid if and only if:

    * It is the empty string,

    * It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid
    strings, or

    * It can be written as `(A)`, where `A` is a valid string.

    You are given a parentheses string `s`. In one move, you can insert a parenthesis at
    any position of the string.

    * For example, if `s = "()))"`, you can insert an opening parenthesis to be
    `"(()))"` or a closing parenthesis to be `"())))"`.

    Return *the minimum number of moves required to make* `s` *valid*.

    """

    def min_add_to_make_valid(self, s: str) -> int:
        stack = []
        # Count of additional parentheses needed
        count = 0

        for char in s:
            if char == "(":
                # Push to stack for each opening parenthesis
                stack.append(char)
            elif char == ")":
                if stack:
                    # If there is an opening parenthesis to match, pop it
                    stack.pop()
                else:
                    # If no matching opening parenthesis, we need to add one
                    count += 1

        # After the loop, any remaining items in stack require closing parentheses
        count += len(stack)

        return count

    minAddToMakeValid = min_add_to_make_valid
