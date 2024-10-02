# https://leetcode.com/problems/rank-transform-of-an-array/


class Solution:
    """1331. Rank Transform of an Array

    Given an array of integers `arr`, replace each element with its rank.

    The rank represents how large the element is. The rank has the following rules:

    * Rank is an integer starting from 1\\.

    * The larger the element, the larger the rank. If two elements are equal, their rank
    must be the same.

    * Rank should be as small as possible.

    """

    def array_rank_transform(self, arr: list[int]) -> list[int]: ...

    arrayRankTransform = array_rank_transform
