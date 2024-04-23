# https://leetcode.com/problems/minimum-height-trees/
from collections import deque


class Solution:
    """310. Minimum Height Trees

    A tree is an undirected graph in which any two vertices are connected by *exactly*
    one path. In other words, any connected graph without simple cycles is a tree.

    Given a tree of `n` nodes labelled from `0` to `n - 1`, and an array of `n - 1`
    `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge
    between the two nodes `ai` and `bi` in the tree, you can choose any node of the tree
    as the root. When you select a node `x` as the root, the result tree has height `h`.
    Among all possible rooted trees, those with minimum height (i.e. `min(h)`)  are
    called **minimum height trees** (MHTs).

    Return *a list of all **MHTs'** root labels*. You can return the answer in **any
    order**.

    The **height** of a rooted tree is the number of edges on the longest downward path
    between the root and a leaf.

    """

    def find_min_height_trees(self, n: int, edges: list[list[int]]) -> list[int]:
        # Count of edges for each node
        counts = [0] * n
        # Link to the adjacent node 
        links = [0] * n
        # Distance from the root
        dists = [0] * n
        # Queue for BFS
        queue = deque()

        # Calculate counts, links, and initialize queue with leaf nodes
        for edge in edges:
            links[edge[0]] ^= edge[1]  # XOR to toggle links
            counts[edge[0]] += 1
            links[edge[1]] ^= edge[0]
            counts[edge[1]] += 1

        for i in range(n):
            if counts[i] == 1:  # Leaf nodes have only one edge
                queue.append(i)

        # Perform BFS to find the minimum height trees
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                temp = queue.popleft()
                links[links[temp]] ^= temp  # Toggle link to parent
                counts[links[temp]] -= 1
                if counts[links[temp]] == 1:
                    dists[links[temp]] = max(step, dists[links[temp]])
                    queue.append(links[temp])
            step += 1

        # Find nodes with maximum distance (minimum height)
        max_dist = max(dists)
        res = [i for i in range(n) if dists[i] == max_dist]

        return res

    findMinHeightTrees = find_min_height_trees
