# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/


class Solution:
    """2940. Find Building Where Alice and Bob Can Meet

    You are given a **0-indexed** array `heights` of positive integers, where
    `heights[i]` represents the height of the `ith` building.

    If a person is in building `i`, they can move to any other building `j` if and only
    if `i < j` and `heights[i] < heights[j]`.

    You are also given another array `queries` where `queries[i] = [ai, bi]`. On the
    `ith` query, Alice is in building `ai` while Bob is in building `bi`.

    Return *an array* `ans` *where* `ans[i]` *is **the index of the leftmost building**
    where Alice and Bob can meet on the* `ith` *query*. *If Alice and Bob cannot move to
    a common building on query* `i`, *set* `ans[i]` *to* `-1`."""

    def leftmost_building_queries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]: ...

    leftmostBuildingQueries = leftmost_building_queries
