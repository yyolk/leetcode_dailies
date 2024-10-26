# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/


class Solution:
    """2458. Height of Binary Tree After Subtree Removal Queries

    You are given the `root` of a **binary tree** with `n` nodes. Each node is assigned
    a unique value from `1` to `n`. You are also given an array `queries` of size `m`.

    You have to perform `m` **independent** queries on the tree where in the `ith` query
    you do the following:

    * **Remove** the subtree rooted at the node with the value `queries[i]` from the
    tree. It is **guaranteed** that `queries[i]` will **not** be equal to the value of
    the root.

    Return *an array* `answer` *of size* `m` *where* `answer[i]` *is the height of the
    tree after performing the* `ith` *query*.

    **Note**:

    * The queries are independent, so the tree returns to its **initial** state after
    each query.

    * The height of a tree is the **number of edges in the longest simple path** from
    the root to some node in the tree.

    Definition for a binary tree node::
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def tree_queries(
        self, root: Optional[TreeNode], queries: list[int]
    ) -> list[int]:
        # Initialize arrays to store heights and node information
        # Heights of leaf nodes
        heights = [0] * 50000
        # Depth of each node
        d = [0] * 100001
        # Left index for each node
        l = [0] * 100001
        # Right index for each node
        r = [0] * 100001
        # Counter for leaf nodes
        len_leaves = 0

        def search(p: TreeNode, h: int) -> None:
            nonlocal len_leaves
            # Store current node's depth
            d[p.val] = h

            # If leaf node found
            if not p.left and not p.right:
                # Store leaf height
                heights[len_leaves] = h
                # Both indices same for leaf
                l[p.val] = r[p.val] = len_leaves
                len_leaves += 1
                return

            # Store left index for current node
            l[p.val] = len_leaves

            # Recursively process left and right subtrees
            if p.left:
                search(p.left, h + 1)
            if p.right:
                search(p.right, h + 1)

            # Store right index for current node
            r[p.val] = len_leaves - 1

        # Process the tree starting from root
        search(root, 0)

        # Total number of leaf nodes
        n = len_leaves
        # Max heights from left
        maxl = [0] * n
        # Max heights from right
        maxr = [0] * n

        # Build prefix and suffix maximum arrays
        for i in range(1, n):
            # Max height from left
            maxl[i] = max(maxl[i-1], heights[i-1])
            # Max height from right
            maxr[n-i-1] = max(maxr[n-i], heights[n-i])

        # Result list
        ret = []

        # Process each query
        for query in queries:
            # Find maximum height excluding current node's subtree
            # Max height to the left
            maxxl = maxl[l[query]]
            # Max height to the right
            maxxr = maxr[r[query]]
            # Result is max of (max left height, max right height, current depth-1)
            ret.append(max(max(maxxl, maxxr), d[query]-1))

        return ret

    treeQueries = tree_queries
