# https://leetcode.com/problems/delete-nodes-and-return-forest/


class Solution:
    """1110. Delete Nodes And Return Forest

    Given the `root` of a binary tree, each node in the tree has a distinct value.

    After deleting all nodes with a value in `to_delete`, we are left with a forest (a
    disjoint union of trees).

    Return the roots of the trees in the remaining forest. You may return the result in
    any order.

    """

    def del_nodes(
        self, root: Optional[TreeNode], to_delete: list[int]
    ) -> list[TreeNode]: ...

    delNodes = del_nodes
