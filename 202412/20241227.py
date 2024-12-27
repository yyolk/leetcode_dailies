# https://leetcode.com/problems/best-sightseeing-pair/


class Solution:
    """1014. Best Sightseeing Pair

    You are given an integer array `values` where values[i] represents the value of the
    `ith` sightseeing spot. Two sightseeing spots `i` and `j` have a **distance** `j -
    i` between them.

    The score of a pair (`i < j`) of sightseeing spots is `values[i] + values[j] + i -
    j`: the sum of the values of the sightseeing spots, minus the distance between them.

    Return *the maximum score of a pair of sightseeing spots*."""

    def max_score_sightseeing_pair(self, values: list[int]) -> int: ...

    maxScoreSightseeingPair = max_score_sightseeing_pair
