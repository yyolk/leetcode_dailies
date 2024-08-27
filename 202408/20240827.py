# https://leetcode.com/problems/path-with-maximum-probability/
import heapq

from collections import defaultdict


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
        # Step 1: Build the graph as an adjacency list
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succ_prob):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Step 2: Initialize the max heap with the start node
        max_heap = [(-1.0, start_node)]
        # Step 3: Track the maximum probability to reach each node
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0
        
        # Step 4: Process the heap until it's empty or we find the end node
        while max_heap:
            # Get the node with the maximum probability so far
            current_prob, current_node = heapq.heappop(max_heap)
            current_prob *= -1  # Convert back to positive
            
            # If we reached the end node, return the probability
            if current_node == end_node:
                return current_prob
            
            # Explore neighbors
            for neighbor, edge_prob in graph[current_node]:
                new_prob = current_prob * edge_prob
                # If the new probability is greater, update and push to the heap
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If we exhaust the heap without finding the end node, return 0.0
        return 0.0

    maxProbability = max_probability
