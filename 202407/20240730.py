# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/


class Solution:
    """1653. Minimum Deletions to Make String Balanced

    You are given a string `s` consisting only of characters `'a'` and `'b'`\u200b\u200b\u200b\u200b.

    You can delete any number of characters in `s` to make `s` **balanced**. `s` is
    **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] =
    'b'` and `s[j]= 'a'`.

    Return *the **minimum** number of deletions needed to make* `s` ***balanced***.

    """

    def minimum_deletions(self, s: str) -> int: ...

    minimumDeletions = minimum_deletions
