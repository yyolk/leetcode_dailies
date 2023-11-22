# https://leetcode.com/problems/validate-binary-tree-nodes/
from collections import defaultdict


class Solution:
    """1361. Validate Binary Tree Nodes

    You have `n` binary tree nodes numbered from `0` to `n - 1` where node `i` has two
    children `left_child[i]` and `right_child[i]`, return `true` if and only if **all**
    the given nodes form **exactly one** valid binary tree.

    If node `i` has no left child then `left_child[i]` will equal `-1`, similarly for the
    right child.

    Note that the nodes have no values and that we only use the node numbers in this
    problem.
    """

    def validate_binary_tree_nodes(
        self, n: int, left_child: list[int], right_child: list[int]
    ) -> bool:
        """Validate if the input nodes form exactly one valid binary tree.

        Proposed solution using DFS.

        Args:
            n (int): The number of binary tree nodes, numbered from 0 to n -1.
            left_child (list of int): The left child for each node.
            right_child (list of int): The right child for each node.

        Returns:
            bool: If the nodes form exactly one valid binary tree.
        """
        # Create an adjacency list to represent the tree structure.
        graph = defaultdict(list)
        # Create an array to keep track of in-degrees for each node.
        in_degree = [0] * n

        # Populate the adjacency list and in-degrees based on left_child and right_child.
        for node in range(n):
            left, right = left_child[node], right_child[node]
            if left != -1:
                # Add left child to the adjacency list of the current node.
                graph[node].append(left)
                # Increment the in-degree of the left child.
                in_degree[left] += 1
            if right != -1:
                # Add right child to the adjacency list of the current node.
                graph[node].append(right)
                # Increment the in-degree of the right child.
                in_degree[right] += 1

        # Find potential root candidates, which are nodes with an in-degree of 0.
        root_candidates = [node for node in range(n) if in_degree[node] == 0]

        # There should be exactly one root candidate for a valid binary tree.
        if len(root_candidates) != 1:
            return False
        root = root_candidates[0]

        # Perform a BFS traversal of the tree to check for cycles and connectivity.
        queue = [root]
        visited = set([root])

        while queue:
            node = queue.pop(0)
            if node in graph:
                for child in graph[node]:
                    # Check if the child has been visited before.
                    if child in visited:
                        return False
                    visited.add(child)
                    queue.append(child)

        # Check if all nodes in the binary tree have been visited.
        return len(visited) == n

    validateBinaryTreeNodes = validate_binary_tree_nodes
