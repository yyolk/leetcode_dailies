# https://leetcode.com/problems/minimum-length-of-string-after-operations/
from collections import Counter


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

    def minimum_length(self, s: str) -> int:
        # Use Counter to count occurrences of each character in the string
        # For each character, if the frequency is odd, we keep one instance,
        # otherwise, we can reduce to 2 (one from each end if all were same)
        return sum(1 if freq % 2 else 2 for freq in Counter(s).values())

    minimumLength = minimum_length
