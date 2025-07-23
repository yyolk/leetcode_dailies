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

    def maximum_gain(self, s: str, x: int, y: int) -> int: ...

    maximumGain = maximum_gain
