# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/


class Solution:
    """2657. Find the Prefix Common Array of Two Arrays

    You are given two **0-indexed** integerpermutations `a` and `b` of length `n`.

    a **prefix common array** of `a` and `b` is an array `C` such that `C[i]` is equal
    to the count of numbers that are present at or before the index `i` in both `a` and
    `b`.

    Return *the **prefix common array** of* `a` *and* `b`.

    a sequence of `n` integers is called a **permutation** if it contains all integers
    from `1` to `n` exactly once."""

    def find_the_prefix_common_array(self, a: list[int], b: list[int]) -> list[int]: ...

    findThePrefixCommonArray = find_the_prefix_common_array
