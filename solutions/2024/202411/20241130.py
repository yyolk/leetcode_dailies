# https://leetcode.com/problems/valid-arrangement-of-pairs/
from collections import defaultdict


class Solution:
    """2097. Valid Arrangement of Pairs

    You are given a **0-indexed** 2D integer array `pairs` where `pairs[i] = [starti,
    endi]`. An arrangement of `pairs` is **valid** if for every index `i` where `1 <= i
    < pairs.length`, we have `endi-1 == starti`.

    Return ***any** valid arrangement of* `pairs`.

    **Note:** The inputs will be generated such that there exists a valid arrangement of
    `pairs`."""

    def valid_arrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        # Create a graph where each node is a city and edges represent paths
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Find the start node (where out_degree > in_degree or start arbitrarily if all are balanced)
        start = pairs[0][0]
        for node in graph:
            if out_degree[node] - in_degree[node] > 0:
                start = node
                break

        def dfs(node, path):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node, path)
            path.append(node)

        # Perform DFS to arrange the pairs
        path = []
        dfs(start, path)
        # Reverse to get correct sequence
        path.reverse()

        # Convert path into pairs format
        result = []
        for i in range(len(path) - 1):
            result.append([path[i], path[i + 1]])

        return result

    validArrangement = valid_arrangement
