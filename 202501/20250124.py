# https://leetcode.com/problems/find-eventual-safe-states/


class Solution:
    """802. Find Eventual Safe States

    There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`.
    The graph is represented by a **0-indexed** 2D integer array `graph` where
    `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an
    edge from node `i` to each node in `graph[i]`.

    A node is a **terminal node** if there are no outgoing edges. A node is a **safe
    node** if every possible path starting from that node leads to a **terminal node**
    (or another safe node).

    Return *an array containing all the **safe nodes** of the graph*. The answer should
    be sorted in **ascending** order."""

    def eventual_safe_nodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)

        # Reverse graph
        reverse_graph = [[] for _ in range(n)]
        out_degree = [0] * n

        for i in range(n):
            for neighbor in graph[i]:
                reverse_graph[neighbor].append(i)
                out_degree[i] += 1

        # Queue for nodes with no outgoing edges
        queue = [i for i in range(n) if out_degree[i] == 0]
        safe_nodes = []

        while queue:
            node = queue.pop(0)
            safe_nodes.append(node)

            for prev_node in reverse_graph[node]:
                out_degree[prev_node] -= 1
                if out_degree[prev_node] == 0:
                    queue.append(prev_node)

        # Sort the safe nodes in ascending order
        return sorted(safe_nodes)

    eventualSafeNodes = eventual_safe_nodes
