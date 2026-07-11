# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/


class Solution:
    """3534. Path Existence Queries in a Graph II

    You are given an integer n representing the number of nodes in a graph,
    labeled from 0 to n-1. You are also given an integer array nums of length n
    and an integer max_diff. An undirected edge exists between nodes i and j if
    the absolute difference between nums[i] and nums[j] is at most max_diff
    (i.e., |nums[i] - nums[j]| <= max_diff). You are also given a 2D integer
    array queries. For each queries[i] = [ui, vi], find the minimum distance
    between nodes ui and vi. If no path exists between the two nodes, return -1
    for that query. Note: The edges between the nodes are unweighted.

    Constraints:
    * 1 <= n == nums.length <= 105
    * 0 <= nums[i] <= 105
    * 0 <= max_diff <= 105
    * 1 <= queries.length <= 105
    * queries[i] == [ui, vi]
    * 0 <= ui, vi < n
    """

    def path_existence_queries(
        self, n: int, nums: list[int], max_diff: int, queries: list[list[int]]
    ) -> list[int]:
        if n == 0:
            return []
        # Sort indices by increasing nums values
        sorted_nodes = sorted(range(n), key=lambda x: nums[x])
        # Assign component ID and local rank in sorted list per node
        comp_id = [-1] * n
        pos_in_comp = [-1] * n
        # Per-component binary lifting tables for max forward reach
        jumps_per_comp = []
        LOG = 18
        cid = 0
        i = 0
        while i < n:
            start = i
            # Extend component while consecutive values differ by <= max_diff
            while i < n and (
                i == start
                or nums[sorted_nodes[i]] - nums[sorted_nodes[i - 1]] <= max_diff
            ):
                i += 1
            comp_nodes = sorted_nodes[start:i]
            m = len(comp_nodes)
            if m == 0:
                continue
            # Compute right[ii]: farthest local index reachable in 1 jump
            far = [0] * m
            j = 0
            for ii in range(m):
                while j < m and nums[comp_nodes[j]] <= nums[comp_nodes[ii]] + max_diff:
                    j += 1
                far[ii] = j - 1
            # Build lifting table: jump[k][ii] = max reach after 2**k jumps
            jump = [[0] * m for _ in range(LOG)]
            for ii in range(m):
                jump[0][ii] = far[ii]
            for k in range(1, LOG):
                for ii in range(m):
                    jump[k][ii] = jump[k - 1][jump[k - 1][ii]]
            jumps_per_comp.append(jump)
            # Record component ID and local rank for each node in comp
            for local in range(m):
                node_idx = comp_nodes[local]
                comp_id[node_idx] = cid
                pos_in_comp[node_idx] = local
            cid += 1
        # Process each query
        answer = []
        for ui, vi in queries:
            if ui == vi:
                answer.append(0)
                continue
            cu = comp_id[ui]
            cv = comp_id[vi]
            if cu != cv:
                answer.append(-1)
                continue
            p1 = pos_in_comp[ui]
            p2 = pos_in_comp[vi]
            if p1 > p2:
                p1, p2 = p2, p1
            jump = jumps_per_comp[cu]
            curr = p1
            dist = 0
            # Greedy lifting: take largest possible 2**k blocks while needed
            for k in range(LOG - 1, -1, -1):
                if jump[k][curr] < p2:
                    curr = jump[k][curr]
                    dist += 1 << k
            # One final single jump if still short of target
            if curr < p2:
                dist += 1
            answer.append(dist)
        return answer

    pathExistenceQueries = path_existence_queries
