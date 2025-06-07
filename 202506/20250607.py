# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/


class Solution:
    """3170. Lexicographically Minimum String After Removing Stars

    You are given a string `s`. It may contain any number of `'*'` characters. Your task
    is to remove all `'*'` characters.

    While there is a `'*'`, do the following operation:

    * Delete the leftmost `'*'` and the **smallest** non-`'*'` character to its *left*.
    If there are several smallest characters, you can delete any of them.

    Return the lexicographically smallest resulting string after removing all `'*'`
    characters."""

    def clear_stars(self, s: str) -> str: ...

    clearStars = clear_stars
