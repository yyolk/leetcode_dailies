# https://leetcode.com/problems/sum-of-distances-in-tree/


class Solution:
    """834. Sum of Distances in Tree

    There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and
    `n - 1` edges.

    You are given the integer `n` and the array `edges` where `edges[i] = [ai, bi]`
    indicates that there is an edge between nodes `ai` and `bi` in the tree.

    Return an array `answer` of length `n` where `answer[i]` is the sum of the distances
    between the `ith` node in the tree and all other nodes.

    """

    def sum_of_distances_in_tree(self, n: int, edges: list[list[int]]) -> list[int]:
        # Initialize a defaultdict to represent the graph
        graph = defaultdict(list)
        # Populate the graph with edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize arrays to store counts and distances
        # count[i] is the number of nodes in subtree rooted at node i
        count = [1] * n
        # result[i] is the sum of distances for subtree rooted at node i
        result = [0] * n
        # total_dist[i] is the sum of distances from node i to all nodes
        total_dist = [0] * n

        # Define a depth-first search (DFS) function to calculate counts and distances
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    result[node] += result[child] + count[child]
                    total_dist[node] += total_dist[child] + count[child]

        # Define a second DFS function to update total distances
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    total_dist[child] = total_dist[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        # Perform the first DFS starting from node 0
        dfs(0, -1)
        # Update total distances using the second DFS
        dfs2(0, -1)

        return total_dist

    sumOfDistancesInTree = sum_of_distances_in_tree
