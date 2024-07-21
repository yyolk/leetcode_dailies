# https://leetcode.com/problems/build-a-matrix-with-conditions/
from collections import defaultdict, deque


class Solution:
    """2392. Build a Matrix With Conditions

    You are given a **positive** integer `k`. You are also given:

    * a 2D integer array `row_conditions` of size `n` where `row_conditions[i] =
    [abovei, belowi]`, and

    * a 2D integer array `col_conditions` of size `m` where `col_conditions[i] = [lefti,
    righti]`.

    The two arrays contain integers from `1` to `k`.

    You have to build a `k x k` matrix that contains each of the numbers from `1` to `k`
    **exactly once**. The remaining cells should have the value `0`.

    The matrix should also satisfy the following conditions:

    * The number `abovei` should appear in a **row** that is strictly **above** the row
    at which the number `belowi` appears for all `i` from `0` to `n - 1`.

    * The number `lefti` should appear in a **column** that is strictly **left** of the
    column at which the number `righti` appears for all `i` from `0` to `m - 1`.

    Return ***any** matrix that satisfies the conditions*. If no answer exists, return
    an empty matrix.

    """

    def build_matrix(
        self, k: int, row_conditions: list[list[int]], col_conditions: list[list[int]]
    ) -> list[list[int]]:
        def topological_sort(k, conditions):
            # Create a graph and in-degree array
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            
            # Build the graph and in-degree array based on conditions
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            
            # Initialize the queue with nodes having zero in-degree
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            topo_order = []
            
            # Perform topological sort using Kahn's algorithm
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            # Check if topological sort is valid (covers all nodes)
            if len(topo_order) == k:
                return topo_order
            else:
                return []
        
        # Get the row order using topological sort
        row_order = topological_sort(k, row_conditions)
        # Get the column order using topological sort
        col_order = topological_sort(k, col_conditions)
        
        # If either row or column order is invalid, return an empty matrix
        if not row_order or not col_order:
            return []
        
        # Map each number to its position in the row order
        row_position = {num: i for i, num in enumerate(row_order)}
        # Map each number to its position in the column order
        col_position = {num: i for i, num in enumerate(col_order)}
        
        # Initialize the k x k matrix with zeros
        matrix = [[0] * k for _ in range(k)]
        
        # Place each number in the matrix according to its row and column positions
        for num in range(1, k + 1):
            matrix[row_position[num]][col_position[num]] = num
        
        return matrix

    buildMatrix = build_matrix
