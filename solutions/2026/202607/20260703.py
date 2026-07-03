# https://leetcode.com/problems/network-recovery-pathways/

from collections import deque


class Solution:
    """3620. Network Recovery Pathways
    Given DAG n nodes 0..n-1, edges[u,v,cost], online[] (0 & n-1 True). Valid
    0->n-1 path: intermediates online + sum costs <=k. Score = min edge cost
    on path. Return max score among valid paths or -1.
    """

    def find_max_path_score(
        self, edges: list[list[int]], online: list[bool], k: int
    ) -> int:
        n = len(online)
        # build adj only online-to-online with costs
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, c in edges:
            if online[u] and online[v]:
                adj[u].append((v, c))
        # indegree only from online edges
        indeg = [0] * n
        for u in range(n):
            if online[u]:
                for v, _ in adj[u]:
                    indeg[v] += 1
        # Kahn topo of online subgraph (valid for all edge subsets)
        q: deque[int] = deque([i for i in range(n) if online[i] and indeg[i] == 0])
        topo: list[int] = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def can_achieve(T: int) -> bool:
            # DAG min-sum DP using edges >=T
            INF = 10**18
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF:
                    continue
                for v, c in adj[u]:
                    if c >= T:
                        if dist[u] + c < dist[v]:
                            dist[v] = dist[u] + c
            return dist[n - 1] <= k

        # binary max T where min-sum path <=k exists
        lo, hi, ans = 0, 10**9, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_achieve(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    findMaxPathScore = find_max_path_score
