# https://leetcode.com/problems/path-with-maximum-probability/
# Repeat of 20240827
import heapq


class Solution:
    """1514. Path with Maximum Probability

    You are given an undirected weighted graph of `n` nodes (0\\-indexed), represented by
    an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes
    `a` and `b` with a probability of success of traversing that edge `succ_prob[i]`.

    Given two nodes `start` and `end`, find the path with the maximum probability of
    success to go from `start` to `end` and return its success probability.

    If there is no path from `start` to `end`, **return 0**. Your answer will be
    accepted if it differs from the correct answer by at most **1e\\-5**.

    """

    def max_probability(
        self,
        n: int,
        edges: list[list[int]],
        succ_prob: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succ_prob):
            graph[a].append((b, prob))
            # Since the graph is undirected
            graph[b].append((a, prob))

        # Initialize max probability array with 0, except for start_node which is 1
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        # Priority queue to store (probability, node)
        pq = [(-1.0, start_node)]  # Start with probability 1 for start_node

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob  # Convert back from max-heap to min-heap behavior

            # If we've reached or exceeded the current max probability for this node,
            # we can skip as we've already found a better path or equal
            if prob < max_prob[node]:
                continue

            # If we've reached the end node, return the probability
            if node == end_node:
                return prob

            # Explore neighbors
            for neighbor, edge_prob in graph[node]:
                # Calculate new probability
                new_prob = prob * edge_prob
                # If this path gives higher probability, update and push to pq
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        # If we've exhausted all paths without reaching end_node
        return 0.0

    maxProbability = max_probability
