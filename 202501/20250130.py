# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
from collections import deque


class Solution:
    """2493. Divide Nodes Into the Maximum Number of Groups

    You are given a positive integer `n` representing the number of nodes in an
    **undirected** graph. The nodes are labeled from `1` to `n`.

    You are also given a 2D integer array `edges`, where `edges[i] = [ai, bi]` indicates
    that there is a **bidirectional** edge between nodes `ai` and `bi`. **Notice** that
    the given graph may be disconnected.

    Divide the nodes of the graph into `m` groups (**1-indexed**) such that:

    * Each node in the graph belongs to exactly one group.

    * For every pair of nodes in the graph that are connected by an edge `[ai, bi]`, if
    `ai` belongs to the group with index `x`, and `bi` belongs to the group with index
    `y`, then `|y - x| = 1`.

    Return *the maximum number of groups (i.e., maximum* `m`*) into which you can divide
    the nodes*. Return `-1` *if it is impossible to group the nodes with the given
    conditions*."""

    def magnificent_sets(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list for the graph, 1-based indexing
        adjacency_list = [[] for _ in range(n + 1)]
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # Track visited nodes to identify connected components
        visited = [False] * (n + 1)
        total_groups = 0

        for node in range(1, n + 1):
            if not visited[node]:
                # Collect all nodes in the current connected component and check bipartiteness
                component_nodes = []
                color = [-1] * (n + 1)
                is_bipartite = True
                queue = deque()
                queue.append(node)
                visited[node] = True
                color[node] = 0
                component_nodes.append(node)

                while queue:
                    current_node = queue.popleft()
                    for neighbor in adjacency_list[current_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            color[neighbor] = color[current_node] ^ 1
                            component_nodes.append(neighbor)
                            queue.append(neighbor)
                        else:
                            if color[neighbor] == color[current_node]:
                                is_bipartite = False

                # If the component is not bipartite, return -1
                if not is_bipartite:
                    return -1

                # Calculate the maximum number of groups for this component
                max_eccentricity = 0
                for start_node in component_nodes:
                    max_distance = 0
                    distance = [-1] * (n + 1)
                    bfs_queue = deque()
                    bfs_queue.append(start_node)
                    distance[start_node] = 0
                    while bfs_queue:
                        current_bfs_node = bfs_queue.popleft()
                        for neighbor in adjacency_list[current_bfs_node]:
                            if distance[neighbor] == -1:
                                distance[neighbor] = distance[current_bfs_node] + 1
                                max_distance = max(max_distance, distance[neighbor])
                                bfs_queue.append(neighbor)
                    # Update maximum eccentricity for the component
                    max_eccentricity = max(max_eccentricity, max_distance + 1)

                # Add the component's contribution to the total groups
                total_groups += max_eccentricity

        return total_groups

    magnificentSets = magnificent_sets
