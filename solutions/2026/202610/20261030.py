# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/


class Solution:
    """3970. Shortest Path With At Most K Consecutive Identical Characters

    You are given an integer `n` representing the number of nodes in a **directed
    weighted** graph, numbered from 0 to `n - 1`. This is represented by a 2D integer
    array `edges`, where `edges[i] = [ui, vi, wi]` represents a directed edge from node
    `ui` to node `vi` with weight `wi`.

    You are also given a string `labels` of length `n`, where `labels[i]` is the
    character assigned to node `i`, and an integer `k`.

    Return the **minimum** **total** edge weight of a path from node 0 to node `n - 1`
    such that the concatenation of the labels of the nodes along the path contains **at
    most** `k` **consecutive** **identical** characters. If no valid path exists, return
    -1.

    Constraints:

    * `1 <= n == labels.length <= 5 * 104`

    * `0 <= edges.length <= 5 * 104`

    * `edges[i] == [ui, vi, wi]`

    * `0 <= ui, vi <= n - 1`

    * `ui != vi`

    * `1 <= wi <= 104`

    * `labels` consists of lowercase English letters

    * `1 <= k <= 50`"""

    def shortest_path(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        """...

        Proposed solution ...

        Args:
            n (int): ...
            edges (list of list of int): ...
            labels (str): ...
            k (int): ...

        Returns:
            int: ..."""
        ...

    shortestPath = shortest_path
