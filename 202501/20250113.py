# https://leetcode.com/problems/minimum-length-of-string-after-operations/


class Solution:
    """3223. Minimum Length of String After Operations

    You are given a string `s`.

    You can perform the following process on `s` **any** number of times:

    * Choose an index `i` in the string such that there is **at least** one character to
    the left of index `i` that is equal to `s[i]`, and **at least** one character to the
    right that is also equal to `s[i]`.

    * Delete the **closest** character to the **left** of index `i` that is equal to
    `s[i]`.

    * Delete the **closest** character to the **right** of index `i` that is equal to
    `s[i]`.

    Return the **minimum** length of the final string `s` that you can achieve."""

    def minimum_length(self, s: str) -> int: ...

    minimumLength = minimum_length
