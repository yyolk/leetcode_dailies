# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/


class Solution:
    """2096. Step-By-Step Directions From a Binary Tree Node to Another

    You are given the `root` of a **binary tree** with `n` nodes. Each node is uniquely
    assigned a value from `1` to `n`. You are also given an integer `start_value`
    representing the value of the start node `s`, and a different integer `dest_value`
    representing the value of the destination node `t`.

    Find the **shortest path** starting from node `s` and ending at node `t`. Generate
    step\\-by\\-step directions of such path as a string consisting of only the
    **uppercase** letters `"L"`, `"R"`, and `"U"`. Each letter indicates a specific
    direction:

    * `"L"` means to go from a node to its **left child** node.

    * `"R"` means to go from a node to its **right child** node.

    * `"U"` means to go from a node to its **parent** node.

    Return *the step\\-by\\-step directions of the **shortest path** from node* `s` *to
    node* `t`.

    Definition for a binary tree node:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def get_directions(
        self, root: Optional[TreeNode], start_value: int, dest_value: int
    ) -> str:
        def find_lca(node: TreeNode, p: int, q: int) -> TreeNode:
            if not node or node.val == p or node.val == q:
                return node
            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        def find_path(node: TreeNode, target: int, path: List[str]) -> bool:
            if not node:
                return False
            if node.val == target:
                return True
            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()
            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()
            return False

        # Find the LCA of start_value and dest_value
        lca = find_lca(root, start_value, dest_value)

        # Find the path from LCA to start_value
        path_to_start = []
        find_path(lca, start_value, path_to_start)

        # Find the path from LCA to dest_value
        path_to_dest = []
        find_path(lca, dest_value, path_to_dest)

        # Convert path_to_start to "U"s
        path_to_start = ["U"] * len(path_to_start)

        # Combine the paths
        return "".join(path_to_start) + "".join(path_to_dest)

    getDirections = get_directions
