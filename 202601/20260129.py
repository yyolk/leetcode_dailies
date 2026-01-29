# https://leetcode.com/problems/minimum-cost-to-convert-string-i


class Solution:
    """2976. Minimum Cost to Convert String I
    
    You are given two 0-indexed strings source and target, both of length n,
    consisting of lowercase English letters. You are also given two 0-indexed
    character arrays original and changed, and an integer array cost, where
    cost[i] represents the cost of changing original[i] to changed[i].
    
    You start with source. In one operation, you can pick a character x from
    the string and change it to y at cost z if there exists j such that
    cost[j] == z, original[j] == x, and changed[j] == y.
    
    Return the minimum cost to convert source to target using any number of
    operations. If impossible, return -1.
    
    Note that there may exist indices i, j such that original[j] ==
    original[i] and changed[j] == changed[i].
    """
    def minimum_cost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        # Model as graph with 26 nodes (lowercase letters)
        # Use Floyd-Warshall for all-pairs shortest paths
        INF = 10**18
        dist = [[INF] * 26 for _ in range(26)]
        
        # Self-distance is 0
        for i in range(26):
            dist[i][i] = 0
        
        # Build direct edges, taking min cost if multiple edges exist
        for orig, chng, cst in zip(original, changed, cost):
            u = ord(orig) - ord("a")
            v = ord(chng) - ord("a")
            dist[u][v] = min(dist[u][v], cst)
        
        # Floyd-Warshall: relax all paths through each intermediate node
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Accumulate min cost for each position
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord("a")
            v = ord(t) - ord("a")
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
        
        return total

    minimumCost = minimum_cost