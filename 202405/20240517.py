# https://leetcode.com/problems/delete-leaves-with-a-given-value/


class Solution:
    """1325. Delete Leaves With a Given Value

    Given a binary tree `root` and an integer `target`, delete all the **leaf nodes**
    with value `target`.

    Note that once you delete a leaf node with value `target`**,** if its parent node
    becomes a leaf node and has the value `target`, it should also be deleted (you need
    to continue doing that until you cannot).

    """

    def remove_leaf_nodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]: ...

    removeLeafNodes = remove_leaf_nodes
