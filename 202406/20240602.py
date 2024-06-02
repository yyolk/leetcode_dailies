# https://leetcode.com/problems/reverse-string/


class Solution:
    """344. Reverse String

    Write a function that reverses a string. The input string is given as an array of
    characters `s`.

    You must do this by modifying the input array [in-
    place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.

    """

    def reverse_string(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

    reverseString = reverse_string