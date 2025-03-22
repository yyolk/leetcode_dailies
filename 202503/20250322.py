# https://leetcode.com/problems/count-the-number-of-complete-components/


class Solution:
    """2685. Count the Number of Complete Components

    You are given an integer `n`. There is an **undirected** graph with `n` vertices,
    numbered from `0` to `n - 1`. You are given a 2D integer array `edges` where
    `edges[i] = [ai, bi]` denotes that there exists an **undirected** edge connecting
    vertices `ai` and `bi`.

    Return *the number of **complete connected components** of the graph*.

    A **connected component** is a subgraph of a graph in which there exists a path
    between any two vertices, and no vertex of the subgraph shares an edge with a vertex
    outside of the subgraph.

    A connected component is said to be **complete** if there exists an edge between
    every pair of its vertices."""

    def count_complete_components(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph: add both directions
        
        # Step 2: Initialize visited array to track explored vertices
        visited = [False] * n
        
        # Step 3: Define DFS to find connected components
        def dfs(vertex, component):
            visited[vertex] = True
            component.append(vertex)
            for neighbor in adj[vertex]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        # Step 4: Count complete components
        complete_count = 0
        
        for vertex in range(n):
            if not visited[vertex]:
                # Find the connected component starting from this vertex
                component = []
                dfs(vertex, component)
                k = len(component)  # Number of vertices in the component
                
                # Count edges within the component
                component_set = set(component)  # For O(1) membership testing
                edge_count = 0
                for v in component:
                    for w in adj[v]:
                        if w in component_set:
                            edge_count += 1
                edge_count //= 2  # Divide by 2 since each edge is counted twice
                
                # Check if the component is complete
                required_edges = k * (k - 1) // 2
                if edge_count == required_edges:
                    complete_count += 1
        
        return complete_count

    countCompleteComponents = count_complete_components
