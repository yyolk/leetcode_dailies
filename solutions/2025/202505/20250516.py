# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/


class Solution:
    """2901. Longest Unequal Adjacent Groups Subsequence II

    You are given a string array `words`, and an array `groups`, both arrays having
    length `n`.

    The **hamming distance** between two strings of equal length is the number of
    positions at which the corresponding characters are **different**.

    You need to select the **longest** subsequence from an array of indices `[0, 1, ...,
    n - 1]`, such that for the subsequence denoted as `[i0, i1, ..., ik-1]` having
    length `k`, the following holds:

    * For **adjacent** indices in the subsequence, their corresponding groups are
    **unequal**, i.e., `groups[ij] != groups[ij+1]`, for each `j` where `0 < j + 1 < k`.

    * `words[ij]` and `words[ij+1]` are **equal** in length, and the **hamming
    distance** between them is `1`, where `0 < j + 1 < k`, for all indices in the
    subsequence.

    Return *a string array containing the words corresponding to the indices **(in
    order)** in the selected subsequence*. If there are multiple answers, return *any of
    them*.

    **Note:** strings in `words` may be **unequal** in length."""

    def get_words_in_longest_subsequence(
        self, words: list[str], groups: list[int]
    ) -> list[str]:
        n = len(words)
        # dp[i] stores the length of the longest valid subsequence ending at index i
        dp = [1] * n
        # prev[i] stores the previous index in the longest subsequence ending at i
        prev = [-1] * n

        # Fill the dp and prev arrays
        for i in range(1, n):
            for j in range(i):
                # Check if words[j] and words[i] have the same length
                if len(words[j]) == len(words[i]) and groups[j] != groups[i]:
                    # Compute Hamming distance
                    hd = sum(a != b for a, b in zip(words[j], words[i]))
                    # If Hamming distance is 1 and extending from j improves the length
                    if hd == 1 and dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # Find the index where the longest subsequence ends
        k = max(range(n), key=lambda x: dp[x])

        # Reconstruct the subsequence
        subseq = []
        while k != -1:
            subseq.append(words[k])
            k = prev[k]
        # Reverse to get the words in increasing order of indices
        subseq.reverse()

        return subseq

    getWordsInLongestSubsequence = get_words_in_longest_subsequence
