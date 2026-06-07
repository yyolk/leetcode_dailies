# https://leetcode.com/problems/create-binary-tree-from-descriptions/


class Solution:
    """2196. Create Binary Tree From Descriptions

    You are given a 2D integer array descriptions where descriptions[i] = [parenti,
    childi, isLefti] indicates that parenti is the parent of childi in a binary tree
    of unique values. Furthermore,
    * If isLefti == 1, then childi is the left child of parenti.
    * If isLefti == 0, then childi is the right child of parenti.
    Construct the binary tree described by descriptions and return its root.
    The test cases will be generated such that the binary tree is valid."""

    def create_binary_tree(self, descriptions: list[list[int]]) -> TreeNode | None:
        # Map value to its TreeNode for quick lookup and creation
        node_map = {}
        # Track all child values to identify root (node with no parent)
        children = set()

        for parent_val, child_val, is_left in descriptions:
            # Create nodes on demand
            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)
            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)

            parent = node_map[parent_val]
            child = node_map[child_val]

            # Link child to correct side of parent
            if is_left:
                parent.left = child
            else:
                parent.right = child

            children.add(child_val)

        # Root is the unique value not appearing as any child
        for val in node_map:
            if val not in children:
                return node_map[val]

        return None

    createBinaryTree = create_binary_tree
