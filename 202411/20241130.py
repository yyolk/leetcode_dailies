# https://leetcode.com/problems/valid-arrangement-of-pairs/


class Solution:
    """2097. Valid Arrangement of Pairs

    You are given a **0-indexed** 2D integer array `pairs` where `pairs[i] = [starti,
    endi]`. An arrangement of `pairs` is **valid** if for every index `i` where `1 <= i
    < pairs.length`, we have `endi-1 == starti`.

    Return ***any** valid arrangement of* `pairs`.

    **Note:** The inputs will be generated such that there exists a valid arrangement of
    `pairs`."""

    def valid_arrangement(self, pairs: list[list[int]]) -> list[list[int]]: ...

    validArrangement = valid_arrangement
