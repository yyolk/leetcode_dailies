# https://leetcode.com/problems/maximum-score-from-removing-substrings/


class Solution:
    """1717. Maximum Score From Removing Substrings

    You are given a string `s` and two integers `x` and `y`. You can perform two types
    of operations any number of times.

    * Remove substring `"ab"` and gain `x` points.

            + For example, when removing `"ab"` from `"cabxbae"` it becomes `"cxbae"`.

    * Remove substring `"ba"` and gain `y` points.

            + For example, when removing `"ba"` from `"cabxbae"` it becomes `"cabxe"`.

    Return *the maximum points you can gain after applying the above operations on* `s`.

    """

    def maximum_gain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, score):
            stack = []
            total_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total_score += score
                else:
                    stack.append(char)
            return "".join(stack), total_score

        if x > y:
            s, score1 = remove_substring(s, 'a', 'b', x)
            _, score2 = remove_substring(s, 'b', 'a', y)
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)
            _, score2 = remove_substring(s, 'a', 'b', x)
        
        return score1 + score2

    maximumGain = maximum_gain
