# https://leetcode.com/problems/minimum-cost-to-convert-string-ii

class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False
        self.pat_id: int = -1

class Solution:
    """
    2977. Minimum Cost to Convert String II
    
    You are given two 0-indexed strings source and target of length n,
    consisting of lowercase English characters. Also given are string arrays
    original and changed, and integer array cost for conversions.
    
    Operations replace substrings with rules, but chosen ranges must be
    disjoint or identical. Return minimum cost to make source into target,
    or -1 if impossible.
    """
    def minimum_cost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        # Collect unique patterns appearing in rules
        patterns = set(original) | set(changed)
        pattern_list = list(patterns)
        num = len(pattern_list)
        id_map = {pattern_list[i]: i for i in range(num)}

        INF = 10**18
        # Initialize transformation cost matrix
        dist = [[INF] * num for _ in range(num)]
        for i in range(num):
            dist[i][i] = 0

        # Add rule edges, taking minimum cost for same conversion
        for o, ch, c in zip(original, changed, cost):
            oid = id_map[o]
            cid = id_map[ch]
            dist[oid][cid] = min(dist[oid][cid], c)

        # Floyd-Warshall: shortest paths between all pattern pairs
        for k in range(num):
            for a in range(num):
                for b in range(num):
                    if dist[a][k] < INF and dist[k][b] < INF:
                        dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

        # Build Trie for all patterns
        root = TrieNode()
        for pid, pat in enumerate(pattern_list):
            node = root
            for char in pat:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.pat_id = pid

        n = len(source)
        # DP: minimum cost to convert prefix ending at index i
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            # Single character skip when characters match
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            # Try longer transformations using Trie on source
            node = root
            j = i
            while j < n and source[j] in node.children:
                node = node.children[source[j]]
                j += 1
                if node.is_end:
                    # Corresponding substring in target
                    t_sub = target[i:j]
                    if t_sub in id_map:
                        bid = id_map[t_sub]
                        aid = node.pat_id
                        c = dist[aid][bid]
                        if c < INF:
                            # Update reachable position with transformation cost
                            dp[j] = min(dp[j], dp[i] + c)

        ans = dp[n]
        return -1 if ans == INF else ans

    minimumCost = minimum_cost