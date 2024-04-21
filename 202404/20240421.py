# https://leetcode.com/problems/find-if-path-exists-in-graph/


class Solution:
    """1971. Find if Path Exists in Graph

    There is a **bi-directional** graph with `n` vertices, where each vertex is labeled
    from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D
    integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional
    edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by **at
    most one** edge, and no vertex has an edge to itself.

    You want to determine if there is a **valid path** that exists from vertex `source`
    to vertex `destination`.

    Given `edges` and the integers `n`, `source`, and `destination`, return `true` *if
    there is a **valid path** from* `source` *to* `destination`*, or* `false`
    *otherwise**.*

    """

    def valid_path(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        # Create an adjacency list representation of the graph
        adjacency_list = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # Perform DFS to check if there is a valid path from source to destination
        visited = [False] * n
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if not visited[node]:
                visited[node] = True
                stack.extend(adjacency_list[node])

        return False

    validPath = valid_path
