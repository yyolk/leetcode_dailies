# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/


class Solution:
    """2900. Longest Unequal Adjacent Groups Subsequence I

    You are given a string array `words` and a **binary** array `groups` both of length
    `n`, where `words[i]` is associated with `groups[i]`.

    Your task is to select the **longest alternating** subsequence from `words`. A
    subsequence of `words` is alternating if for any two consecutive strings in the
    sequence, their corresponding elements in the binary array `groups` differ.
    Essentially, you are to choose strings such that adjacent elements have non-matching
    corresponding bits in the `groups` array.

    Formally, you need to find the longest subsequence of an array of indices `[0, 1,
    ..., n - 1]` denoted as `[i0, i1, ..., ik-1]`, such that `groups[ij] !=
    groups[ij+1]` for each `0 <= j < k - 1` and then find the words corresponding to
    these indices.

    Return *the selected subsequence. If there are multiple answers, return **any** of
    them.*

    **Note:** The elements in `words` are distinct."""

    def get_longest_subsequence(self, words: list[str], groups: list[int]) -> list[str]:
        # Initialize the result with the first word
        result = [words[0]]
        # Track the group of the last included word
        last_group = groups[0]

        # Iterate through the remaining words starting from index 1
        for i in range(1, len(words)):
            # If the current group differs from the last included group
            if groups[i] != last_group:
                # Add the current word to the subsequence
                result.append(words[i])
                # Update the last_group to the current group
                last_group = groups[i]

        return result

    getLongestSubsequence = get_longest_subsequence
