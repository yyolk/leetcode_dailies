# https://leetcode.com/problems/distinct-subsequences-ii/


class Solution:
    """940. Distinct Subsequences II

    Given a string s, return the number of distinct non-empty subsequences of s.
    Since the answer may be very large, return it modulo 10^9 + 7.

    A subsequence of a string is a new string that is formed from the original
    string by deleting some (can be none) of the characters without disturbing
    the relative positions of the remaining characters. (i.e., "ace" is a
    subsequence of "abcde" while "aec" is not.

    Constraints:

    * 1 <= s.length <= 2000

    * s consists of lowercase English letters.
    """

    def distinct_subseq_i_i(self, s: str) -> int:
        MOD = 10**9 + 7
        # last[c] = number of distinct subsequences ending with char c
        last = [0] * 26
        total = 0  # total distinct non-empty subsequences so far
        for ch in s:
            idx = ord(ch) - ord("a")
            prev = last[idx]
            # New subsequences ending with this char: all existing + singleton
            last[idx] = (total + 1) % MOD
            # Add the net new ones (subtract the previous ending with same char)
            total = (total + last[idx] - prev + MOD) % MOD
        return total

    distinctSubseqII = distinct_subseq_i_i
