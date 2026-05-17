# https://leetcode.com/problems/is-subsequence/


class Solution:
    """392. Is Subsequence

    Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*,
    or* `false` *otherwise*.

    A **subsequence** of a string is a new string that is formed from the original string by
    deleting some (can be none) of the characters without disturbing the relative positions
    of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"`
    is not).
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        """Determines if s is a subsequence of t

        Proposed solution two pointers.

        Args:
            s (str): string input to determine if subsequence
            t (str): string input to match subsequence against

        Returns:
            bool: whether or not s is a subsequence of t
        """
        # Avoid computing this case
        if len(s) > len(t):
            return False

        # Instantiate pointers for characters of each string
        s_ptr, t_ptr = 0, 0

        # Scan each input at the same time, while not disturbing relative positions
        while s_ptr < len(s) and t_ptr < len(t):
            # We've found a match
            if s[s_ptr] == t[t_ptr]:
                # Move s_ptr forward
                s_ptr += 1
            # Move t_ptr forward, we may have found a match before
            t_ptr += 1

        # s is a subsequence of t if our s_ptr is the length of s
        return s_ptr == len(s)
