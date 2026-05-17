# https://leetcode.com/problems/word-subsets/
from collections import Counter


class Solution:
    """916. Word Subsets

    You are given two string arrays `words1` and `words2`.

    A string `b` is a **subset** of string `a` if every letter in `b` occurs in `a`
    including multiplicity.

    * For example, `"wrr"` is a subset of `"warrior"` but is not a subset of `"world"`.

    A string `a` from `words1` is **universal** if for every string `b` in `words2`, `b`
    is a subset of `a`.

    Return an array of all the **universal** strings in `words1`. You may return the
    answer in **any order**."""

    def word_subsets(self, words1: list[str], words2: list[str]) -> list[str]:
        # First, compute the maximum frequency needed for each character across all words in words2
        bmax = {}
        for b in words2:
            count_b = Counter(b)
            for c in count_b:
                bmax[c] = max(bmax.get(c, 0), count_b[c])

        # Check if each word in words1 is universal
        result = []
        for a in words1:
            count_a = Counter(a)
            if all(count_a[c] >= bmax.get(c, 0) for c in bmax):
                result.append(a)
        return result

    wordSubsets = word_subsets
