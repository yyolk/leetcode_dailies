# https://leetcode.com/problems/xor-queries-of-a-subarray/


class Solution:
    """1310. XOR Queries of a Subarray

    You are given an array `arr` of positive integers. You are also given the array
    `queries` where `queries[i] = [lefti, righti]`.

    For each query `i` compute the **XOR** of elements from `lefti` to `righti` (that
    is, `arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti]` ).

    Return an array `answer` where `answer[i]` is the answer to the `ith` query.

    """

    def xor_queries(self, arr: list[int], queries: list[list[int]]) -> list[int]: ...

    xorQueries = xor_queries
