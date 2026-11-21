# https://leetcode.com/problems/find-subtree-sizes-after-changes/


class Solution:
    """3331. Find Subtree Sizes After Changes

    You are given a tree rooted at node 0 that consists of `n` nodes numbered from `0`
    to `n - 1`. The tree is represented by an array `parent` of size `n`, where
    `parent[i]` is the parent of node `i`. Since node 0 is the root, `parent[0] == -1`.

    You are also given a string `s` of length `n`, where `s[i]` is the character
    assigned to node `i`.

    We make the following changes on the tree **one** time **simultaneously** for all
    nodes `x` from `1` to `n - 1`:

    * Find the **closest** node `y` to node `x` such that `y` is an ancestor of `x`, and
    `s[x] == s[y]`.

    * If node `y` does not exist, do nothing.

    * Otherwise, **remove** the edge between `x` and its current parent and make node
    `y` the new parent of `x` by adding an edge between them.

    Return an array `answer` of size `n` where `answer[i]` is the **size** of the
    subtree rooted at node `i` in the **final** tree.

    Constraints:

    * `n == parent.length == s.length`

    * `1 <= n <= 105`

    * `0 <= parent[i] <= n - 1` for all `i >= 1`.

    * `parent[0] == -1`

    * `parent` represents a valid tree.

    * `s` consists only of lowercase English letters.
    """

    def find_subtree_sizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        # Build children lists from the original parent array.
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        # Compute new parents by finding closest same-character ancestors via DFS.
        new_parent = parent[:]
        # Track the most recent ancestor index for each character.
        last = [-1] * 26

        def dfs(node: int) -> None:
            char_idx = ord(s[node]) - ord("a")
            # If a closer same-char ancestor exists, reparent this node to it.
            if last[char_idx] != -1:
                new_parent[node] = last[char_idx]
            # Record this node as the latest for its character, then recurse.
            prev = last[char_idx]
            last[char_idx] = node
            for child in children[node]:
                dfs(child)
            # Restore the previous last-seen for backtracking.
            last[char_idx] = prev

        dfs(0)

        # Build the adjacency list for the final tree after reparenting.
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Compute subtree sizes bottom-up via DFS on the new tree.
        sizes = [0] * n

        def compute_size(node: int) -> int:
            size = 1
            for child in new_children[node]:
                size += compute_size(child)
            sizes[node] = size
            return size

        compute_size(0)
        return sizes

    findSubtreeSizes = find_subtree_sizes
