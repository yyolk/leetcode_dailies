# https://leetcode.com/problems/longest-subsequence-repeated-k-times/
import collections


class Solution:
    """2014. Longest Subsequence Repeated k Times

    You are given a string `s` of length `n`, and an integer `k`. You are tasked to find
    the **longest subsequence repeated** `k` times in string `s`.

    A **subsequence** is a string that can be derived from another string by deleting
    some or no characters without changing the order of the remaining characters.

    A subsequence `seq` is **repeated** `k` times in the string `s` if `seq * k` is a
    subsequence of `s`, where `seq * k` represents a string constructed by concatenating
    `seq` `k` times.

    * For example, `"bba"` is repeated `2` times in the string `"bababcba"`, because the
    string `"bbabba"`, constructed by concatenating `"bba"` `2` times, is a subsequence
    of the string `"bababcba"`.

    Return *the **longest subsequence repeated*** `k` *times in string* `s`*. If
    multiple such subsequences are found, return the **lexicographically largest** one.
    If there is no such subsequence, return an **empty** string*."""

    def longest_subsequence_repeated_k(self, s: str, k: int) -> str:
        # Step 1: Calculate frequency of each character in s
        count_s = collections.Counter(s)
        # Maximum frequency each character can have in seq
        max_count = {c: count_s[c] // k for c in count_s if count_s[c] >= k}
        if not max_count:
            return ""

        # Step 2: Determine maximum possible length of subsequence
        max_len = len(s) // k

        # Step 3: Function to check if seq * k is a subsequence of s
        def is_subsequence(seq):
            if not seq:
                return True
            seq_k = seq * k
            i = 0
            for c in s:
                if i < len(seq_k) and c == seq_k[i]:
                    i += 1
            return i == len(seq_k)

        # Step 4: Generate candidates using backtracking
        def backtrack(curr, length, count):
            if len(curr) == length:
                if is_subsequence(curr):
                    return curr
                return ""
            # Try characters from 'z' to 'a' for lexicographically largest
            for c in sorted(max_count.keys(), reverse=True):
                if count[c] < max_count[c]:
                    count[c] += 1
                    result = backtrack(curr + c, length, count)
                    if result:
                        return result
                    count[c] -= 1
            return ""

        # Step 5: Try each length from max_len down to 0
        count = collections.defaultdict(int)
        for length in range(max_len, -1, -1):
            result = backtrack("", length, count)
            if result:
                return result
        return ""

    longestSubsequenceRepeatedK = longest_subsequence_repeated_k
