# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/


class Solution:
    """3841. Palindromic Path Queries in a Tree

    You are given an undirected tree with n nodes labeled 0 to n - 1. This is
    represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi]
    indicates an undirected edge between nodes ui and vi.

    You are also given a string s of length n consisting of lowercase English
    letters, where s[i] represents the character assigned to node i.

    You are also given a string array queries, where each queries[i] is either:

    * "update ui c": Change the character at node ui to c. Formally, update
      s[ui] = c.

    * "query ui vi": Determine whether the string formed by the characters on
      the unique path from ui to vi (inclusive) can be rearranged into a
      palindrome.

    Return a boolean array answer, where answer[j] is true if the jth query of
    type "query ui vi" can be rearranged into a palindrome, and false otherwise.

    Constraints:

    * 1 <= n == s.length <= 5 * 10^4

    * edges.length == n - 1

    * edges[i] = [ui, vi]

    * 0 <= ui, vi <= n - 1

    * s consists of lowercase English letters.

    * The input is generated such that edges represents a valid tree.

    * 1 <= queries.length <= 5 * 10^4

      + queries[i] = "update ui c" or

      + queries[i] = "query ui vi"

      + 0 <= ui, vi <= n - 1

      + c is a lowercase English letter.
    """

    def palindrome_path(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        # Build adjacency list for the tree.
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # HLD structures: parent, depth, size, heavy, head, position.
        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        cur_pos = [0]

        # DFS to compute subtree sizes and heavy children.
        def dfs(u: int, p: int) -> None:
            parent[u] = p
            for v in adj[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)
                size[u] += size[v]
                if heavy[u] == -1 or size[v] > size[heavy[u]]:
                    heavy[u] = v

        # Decompose tree into heavy chains and assign positions.
        def decompose(u: int, h: int) -> None:
            head[u] = h
            pos[u] = cur_pos[0]
            cur_pos[0] += 1
            if heavy[u] != -1:
                decompose(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    decompose(v, v)

        if n:
            dfs(0, -1)
            decompose(0, 0)

        # Iterative segment tree for range XOR of 26-bit character masks.
        tree_size = 1
        while tree_size < n:
            tree_size <<= 1
        tree = [0] * (2 * tree_size)

        # Place initial node masks into leaves according to HLD positions.
        for i in range(n):
            tree[tree_size + pos[i]] = 1 << (ord(s[i]) - ord("a"))
        for i in range(tree_size - 1, 0, -1):
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

        def update(idx: int, value: int) -> None:
            # Point-update the mask at the given HLD position.
            idx += tree_size
            tree[idx] = value
            idx >>= 1
            while idx:
                tree[idx] = tree[2 * idx] ^ tree[2 * idx + 1]
                idx >>= 1

        def query_range(left: int, right: int) -> int:
            # Compute XOR of masks in the HLD position range [left, right].
            res = 0
            left += tree_size
            right += tree_size
            while left <= right:
                if left & 1:
                    res ^= tree[left]
                    left += 1
                if not (right & 1):
                    res ^= tree[right]
                    right -= 1
                left >>= 1
                right >>= 1
            return res

        def query_path(u: int, v: int) -> int:
            # XOR all node masks on the unique path from u to v.
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query_range(pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_range(pos[u], pos[v])
            return res

        answers: list[bool] = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                node = int(parts[1])
                ch = parts[2]
                # Update the character mask for the node.
                update(pos[node], 1 << (ord(ch) - ord("a")))
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                # True iff at most one character has odd frequency.
                answers.append((mask & (mask - 1)) == 0)

        return answers

    palindromePath = palindrome_path
