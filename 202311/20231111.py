# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
import heapq


class Graph:
    """2642. Design Graph With Shortest Path Calculator

    There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1.
    The edges of the graph are initially represented by the given array edges where 
    edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi
    with the cost edgeCosti.

    Implement the Graph class:

    * Graph(int n, int[][] edges) initializes the object with n nodes and the given
    edges.
    * addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost].
    It is guaranteed that there is no edge between the two nodes before adding this one.
    * int shortestPath(int node1, int node2) returns the minimum cost of a path from
    node1 to node2. If no path exists, return -1. The cost of a path is the sum of the
    costs of the edges in the path.

    Your Graph object will be instantiated and called as such:

        obj = Graph(n, edges)
        obj.addEdge(edge)
        param_2 = obj.shortestPath(node1,node2)
    """
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.adjacency_list = {}

        for edge in edges:
            from_node, to_node, cost = edge
            if from_node not in self.adjacency_list:
                self.adjacency_list[from_node] = []
            self.adjacency_list[from_node].append((to_node, cost))

    def add_edge(self, edge: list[int]):
        from_node, to_node, cost = edge
        if from_node not in self.adjacency_list:
            self.adjacency_list[from_node] = []
        self.adjacency_list[from_node].append((to_node, cost))

    def shortest_path(self, node1: int, node2: int) -> int:
        min_heap = [(0, node1)]
        visited = set()

        while min_heap:
            current_cost, current_node = heapq.heappop(min_heap)

            if current_node == node2:
                return current_cost

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node in self.adjacency_list:
                for neighbor, edge_cost in self.adjacency_list[current_node]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (current_cost + edge_cost, neighbor))

        # If no path exists
        return -1

    shortestPath = shortest_path
    addEdge = add_edge
