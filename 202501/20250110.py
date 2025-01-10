# https://leetcode.com/problems/word-subsets/


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

    def word_subsets(self, words1: list[str], words2: list[str]) -> list[str]: ...

    wordSubsets = word_subsets
