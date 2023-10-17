# https://leetcode.com/problems/validate-binary-tree-nodes/


class Solution:
    """1361. Validate Binary Tree Nodes

    You have `n` binary tree nodes numbered from `0` to `n - 1` where node `i` has two
    children `leftChild[i]` and `rightChild[i]`, return `true` if and only if **all**
    the given nodes form **exactly one** valid binary tree.

    If node `i` has no left child then `leftChild[i]` will equal `-1`, similarly for the
    right child.

    Note that the nodes have no values and that we only use the node numbers in this
    problem.
    """

    def validate_binary_tree_nodes(
        self, n: int, left_child: List[int], right_child: List[int]
    ) -> bool:
        ...

    validateBinaryTreeNodes = validate_binary_tree_nodes