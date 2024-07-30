# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/


class Solution:
    """1653. Minimum Deletions to Make String Balanced

    You are given a string `s` consisting only of characters `"a"` and `"b"`\u200b\u200b\u200b\u200b.

    You can delete any number of characters in `s` to make `s` **balanced**. `s` is
    **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] =
    "b"` and `s[j]= "a"`.

    Return *the **minimum** number of deletions needed to make* `s` ***balanced***.

    """

    def minimum_deletions(self, s: str) -> int:
        # Initialize the minimum deletions needed to make the string balanced
        min_deletions = 0
        # Initialize the count of "b" characters seen so far
        count = 0
        # Traverse the string
        for i in s:
            # If the current character is "b"
            if i == "b":
                # Increment the count of "b" characters
                count += 1
            # If the current character is "a" and there are "b"s before it
            elif count:
                # Increment the minimum deletions needed
                min_deletions += 1
                # Decrement the count of "b" characters since one "b" is balanced by this "a"
                count -= 1
        # Return the minimum deletions needed to make the string balanced
        return min_deletions

    minimumDeletions = minimum_deletions
