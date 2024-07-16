# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/


class Solution:
    """2096. Step-By-Step Directions From a Binary Tree Node to Another

    You are given the `root` of a **binary tree** with `n` nodes. Each node is uniquely
    assigned a value from `1` to `n`. You are also given an integer `start_value`
    representing the value of the start node `s`, and a different integer `dest_value`
    representing the value of the destination node `t`.

    Find the **shortest path** starting from node `s` and ending at node `t`. Generate
    step\\-by\\-step directions of such path as a string consisting of only the
    **uppercase** letters `'L'`, `'R'`, and `'U'`. Each letter indicates a specific
    direction:

    * `'L'` means to go from a node to its **left child** node.

    * `'R'` means to go from a node to its **right child** node.

    * `'U'` means to go from a node to its **parent** node.

    Return *the step\\-by\\-step directions of the **shortest path** from node* `s` *to
    node* `t`.

    """

    def get_directions(
        self, root: Optional[TreeNode], start_value: int, dest_value: int
    ) -> str: ...

    getDirections = get_directions
