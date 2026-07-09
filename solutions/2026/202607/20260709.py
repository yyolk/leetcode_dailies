# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

class Solution:
    """3532. Path Existence Queries in a Graph I

    You are given an integer n representing the number of nodes in a graph,
    labeled from 0 to n-1. You are also given an integer array nums of length
    n sorted in non-decreasing order, and an integer max_diff. An undirected
    edge exists between nodes i and j if |nums[i] - nums[j]| <= max_diff.
    You are also given a 2D integer array queries. For each queries[i]=[ui,vi],
    determine whether there exists a path between ui and vi. Return a boolean
    array answer where answer[i] is true if a path exists for the ith query.
    Constraints: 1<=n==nums.length<=1e5, nums sorted non-dec, 0<=max_diff<=1e5,
    1<=queries.length<=1e5, 0<=ui,vi<n.
    """
    def path_existence_queries(
        self, n: int, nums: list[int], max_diff: int, queries: list[list[int]]
    ) -> list[bool]:
        # comp[i] = ID of contiguous component containing node i
        comp = [0] * n
        curr_comp = 0
        for i in range(1, n):
            # gap > max_diff splits components: no cross-gap edges possible
            # (sorted nums ensures left-max <= nums[i-1], right-min >= nums[i])
            if nums[i] - nums[i - 1] > max_diff:
                curr_comp += 1
            comp[i] = curr_comp
        # path exists iff u and v share component (chain of <=max_diff edges)
        return [comp[u] == comp[v] for u, v in queries]

    pathExistenceQueries = path_existence_queries
