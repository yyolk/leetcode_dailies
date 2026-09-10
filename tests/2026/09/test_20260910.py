class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Build a binary tree from level-order list (None for missing nodes)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def test_average_of_subtree_examples(solution):
    # Example 1
    root = build_tree([4, 8, 5, 0, 1, None, 6])
    assert solution.averageOfSubtree(root) == 5

    # Example 2
    root = build_tree([1])
    assert solution.averageOfSubtree(root) == 1
