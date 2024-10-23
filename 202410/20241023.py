# https://leetcode.com/problems/cousins-in-binary-tree-ii/


class Solution:
    """2641. Cousins in Binary Tree II

    Given the `root` of a binary tree, replace the value of each node in the tree with
    the **sum of all its cousins' values**.

    Two nodes of a binary tree are **cousins** if they have the same depth with
    different parents.

    Return *the* `root` *of the modified tree*.

    **Note** that the depth of a node is the number of edges in the path from the root
    node to it.

    """

    def replace_value_in_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: ...

    replaceValueInTree = replace_value_in_tree
