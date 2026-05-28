# https://leetcode.com/problems/longest-common-suffix-queries/


class Solution:
    """3093. Longest Common Suffix Queries

    You are given two arrays of strings `words_container` and `words_query`.

    For each `words_query[i]`, you need to find a string from `words_container` that has
    the **longest common suffix** with `words_query[i]`. If there are two or more
    strings in `words_container` that share the longest common suffix, find the string
    that is the **smallest** in length. If there are two or more such strings that have
    the **same** smallest length, find the one that occurred **earlier** in
    `words_container`.

    Return *an array of integers* `ans`*, where* `ans[i]` *is the index of the string
    in* `words_container` *that has the **longest common suffix** with*
    `words_query[i]`*.*"""

    def string_indices(
        self, words_container: list[str], words_query: list[str]
    ) -> list[int]: ...

    stringIndices = string_indices
