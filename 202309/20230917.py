# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
from collections import deque


class Solution:
    """847. Shortest Path Visiting All Nodes

    You have an undirected, connected graph of `n` nodes labeled from `0` to `n - 1`. You
    are given an array `graph` where `graph[i]` is a list of all the nodes connected with
    node `i` by an edge.

    Return *the length of the shortest path that visits every node*. You may start and stop
    at any node, you may revisit nodes multiple times, and you may reuse edges.
    """

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """The shortest path that visits every node in graph

        Proposed solution uses breadth-first search and bitmasking.
        via https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/4053514/94-74-bfs-bitmask/?envType=daily-question&envId=2023-09-17

        Args:
            graph (List of List of int): input where graph[i] is a list of all nodes
                connected with node i by an edge

        Returns:
            int: the shortest path that will visit each node
        """
        n = len(graph)
        # Initialize a double-ended queue, filled with bit-shifted values
        queue = deque([(1 << i, i, 0) for i in range(n)])
        # Initialize a set with explored values up to length
        visited = set((1 << i, i) for i in range(n))

        while queue:
            # Take a state from the front of the queue
            mask, node, distance = queue.popleft()
            # Check if all nodes have been visited
            if mask == (1 << n) - 1:
                # Return our computed distance, all nodes have been visited
                return distance
            # If we continue, we'll explore the neighbors
            # The neighbor is the new_node
            for neighbor in graph[node]:
                # Update the mask to include the neighbor as visited
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    # Increment the distance, and enqueue the new node and new_mask
                    queue.append((new_mask, neighbor, distance + 1))
