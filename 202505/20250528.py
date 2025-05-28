# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
from collections import deque


class Solution:
    """3372. Maximize the Number of Target Nodes After Connecting Trees I

    There exist two **undirected** trees with `n` and `m` nodes, with **distinct**
    labels in ranges `[0, n - 1]` and `[0, m - 1]`, respectively.

    You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m
    - 1`, respectively, where `edges1[i] = [ai, bi]` indicates that there is an edge
    between nodes `ai` and `bi` in the first tree and `edges2[i] = [ui, vi]` indicates
    that there is an edge between nodes `ui` and `vi` in the second tree. You are also
    given an integer `k`.

    Node `u` is **target** to node `v` if the number of edges on the path from `u` to
    `v` is less than or equal to `k`. **Note** that a node is *always* **target** to
    itself.

    Return an array of `n` integers `answer`, where `answer[i]` is the **maximum**
    possible number of nodes **target** to node `i` of the first tree if you have to
    connect one node from the first tree to another node in the second tree.

    **Note** that queries are independent from each other. That is, for every query you
    will remove the added edge before proceeding to the next query."""

    def max_target_nodes(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]:
        # Build adjacency lists for both trees
        g1 = self.build_graph(edges1)
        g2 = self.build_graph(edges2)
        
        # If k is 0, each node is only target to itself
        if k == 0:
            return [1] * len(g1)
        
        # Count nodes within distance k from each node in the first tree
        cnt1 = self.bfs_count_max(g1, k)
        
        # Count nodes within distance k-1 from each node in the second tree
        cnt2 = self.bfs_count_max(g2, k - 1)
        
        # Find the maximum number of nodes within distance k-1 in the second tree
        max_cnt2 = max(cnt2)
        
        # Compute the answer for each node by adding its count to the maximum from the second tree
        return [cnt + max_cnt2 for cnt in cnt1]

    def build_graph(self, edges: List[List[int]]) -> List[List[int]]:
        # Calculate number of nodes (number of edges + 1)
        n = len(edges) + 1
        # Initialize adjacency list for the graph
        graph = [[] for _ in range(n)]
        # Add edges to the adjacency list (undirected graph)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # Return the constructed graph
        return graph

    def bfs_count_max(self, graph: list[list[int]], max_dist: int) -> list[int]:
        # Get the number of nodes in the graph
        n = len(graph)
        # Initialize result array to store counts for each starting node
        result = [0] * n
        # Iterate over each node as the starting point
        for start in range(n):
            # Initialize visited array to track explored nodes
            visited = [False] * n
            # Create a queue for BFS with (node, distance) pairs
            q = deque()
            # Start with the current node at distance 0
            q.append((start, 0))
            # Mark the starting node as visited
            visited[start] = True
            # Initialize count with 1 for the starting node itself
            count = 1
            # Perform BFS
            while q:
                # Get the current node and its distance from the start
                node, dist = q.popleft()
                # If distance equals max_dist, stop exploring further from this node
                if dist == max_dist:
                    continue
                # Explore all neighbors of the current node
                for neighbor in graph[node]:
                    # If neighbor hasn't been visited
                    if not visited[neighbor]:
                        # Mark it as visited
                        visited[neighbor] = True
                        # Add it to the queue with increased distance
                        q.append((neighbor, dist + 1))
                        # Increment the count of reachable nodes
                        count += 1
            # Store the total count for this starting node
            result[start] = count
        # Return the array of counts
        return result

    maxTargetNodes = max_target_nodes
