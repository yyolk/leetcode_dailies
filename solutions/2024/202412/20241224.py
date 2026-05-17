# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/


class Solution:
    """3203. Find Minimum Diameter After Merging Two Trees

    There exist two **undirected** trees with `n` and `m` nodes, numbered from `0` to `n
    - 1` and from `0` to `m - 1`, respectively. You are given two 2D integer arrays
    `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i]
    = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the first
    tree and `edges2[i] = [ui, vi]` indicates that there is an edge between nodes `ui`
    and `vi` in the second tree.

    You must connect one node from the first tree with another node from the second tree
    with an edge.

    Return the **minimum** possible **diameter** of the resulting tree.

    The **diameter** of a tree is the length of the *longest* path between any two nodes
    in the tree."""

    def minimum_diameter_after_merge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        def diameter_and_farthest_nodes(graph):
            """Helper function to compute the diameter and the farthest nodes of a tree."""

            def bfs(start):
                queue = [(start, 0)]
                visited = set()
                farthest_node = start
                max_distance = 0

                while queue:
                    node, dist = queue.pop(0)
                    if node not in visited:
                        visited.add(node)
                        if dist > max_distance:
                            max_distance = dist
                            farthest_node = node
                        for neighbor in graph[node]:
                            if neighbor not in visited:
                                queue.append((neighbor, dist + 1))
                return farthest_node, max_distance

            # Find the farthest node from an arbitrary starting point
            start_node = 0
            farthest_node, _ = bfs(start_node)
            # Perform BFS again from the farthest node to get the diameter
            other_end, tree_diameter = bfs(farthest_node)
            return tree_diameter, (farthest_node, other_end)

        # Build adjacency lists for both trees
        graph1 = {i: [] for i in range(len(edges1) + 1)}
        graph2 = {i: [] for i in range(len(edges2) + 1)}

        for a, b in edges1:
            graph1[a].append(b)
            graph1[b].append(a)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        # Calculate diameters and farthest nodes of both trees
        diam1, ends1 = diameter_and_farthest_nodes(graph1)
        diam2, ends2 = diameter_and_farthest_nodes(graph2)

        # Minimum diameter after merging
        return max((diam1 + 1) // 2 + (diam2 + 1) // 2 + 1, max(diam1, diam2))

    minimumDiameterAfterMerge = minimum_diameter_after_merge
