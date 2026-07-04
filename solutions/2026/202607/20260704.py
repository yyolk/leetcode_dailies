# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

from collections import deque


class Solution:
    """2492. Minimum Score of a Path Between Two Cities

    You are given a positive integer n representing n cities numbered from 1 to
    n. Also given 2D roads where roads[i]=[ai,bi,distancei] for bidirectional
    road ai-bi with distance distancei. Graph not necessarily connected. Score
    of path = min road distance on it. Return min possible score for any path
    1 to n (repeats of roads/cities allowed). Guaranteed at least one path.
    """

    def min_score(self, n: int, roads: list[list[int]]) -> int:
        # adj list: each node -> list of (neighbor, weight)
        adj = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))

        # BFS explores entire component of 1 (includes n)
        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        ans = float("inf")

        while q:
            u = q.popleft()
            for v, d in adj[u]:
                # all edges incident to reachable nodes are in component
                # (undirected => no external edges possible)
                ans = min(ans, d)
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        return ans

    minScore = min_score
