# https://leetcode.com/problems/find-champion-ii/


class Solution:
    """2924. Find Champion II

    There are `n` teams numbered from `0` to `n - 1` in a tournament; each team is also
    a node in a **DAG**.

    You are given the integer `n` and a **0-indexed** 2D integer array `edges` of length
    `m` representing the **DAG**, where `edges[i] = [ui, vi]` indicates that there is a
    directed edge from team `ui` to team `vi` in the graph.

    A directed edge from `a` to `b` in the graph means that team `a` is **stronger**
    than team `b` and team `b` is **weaker** than team `a`.

    Team `a` will be the **champion** of the tournament if there is no team `b` that is
    **stronger** than team `a`.

    Return *the team that will be the **champion** of the tournament if there is a
    **unique** champion, otherwise, return* `-1`*.*

    **Notes**

    * A **cycle** is a series of nodes `a1, a2, ..., an, an+1` such that node `a1` is
    the same node as node `an+1`, the nodes `a1, a2, ..., an` are distinct, and there is
    a directed edge from the node `ai` to node `ai+1` for every `i` in the range `[1,
    n]`.

    * A **DAG** is a directed graph that does not have any **cycle**."""

    def find_champion(self, n: int, edges: list[list[int]]) -> int:
        # Create an adjacency list to keep track of teams that are stronger than others
        stronger_than = [set() for _ in range(n)]

        # Populate the adjacency list
        for u, v in edges:
            stronger_than[u].add(v)

        # Function to check if team 'a' is stronger than team 'b'
        def is_stronger_than(a, b):
            return b in stronger_than[a]

        # Check each team if it could be the champion
        for i in range(n):
            # Check if there's any team stronger than i
            if all(not is_stronger_than(j, i) for j in range(n) if j != i):
                # Check if there's only one champion
                for j in range(n):
                    if i != j and all(not is_stronger_than(k, j) for k in range(n) if k != j):
                        # More than one champion
                        return -1
                return i

        # If we've gone through all teams and haven't returned, there's no unique champion
        return -1

    findChampion = find_champion
