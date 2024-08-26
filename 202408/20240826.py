# https://leetcode.com/problems/n-ary-tree-postorder-traversal/


class Solution:
    """590. N-ary Tree Postorder Traversal

    Given the `root` of an n\\-ary tree, return *the postorder traversal of its nodes'
    values*.

    Nary\\-Tree input serialization is represented in their level order traversal. Each
    group of children is separated by the null value (See examples)

    Definition for a Node::
        class Node:
            def __init__(self, val=None, children=None):
                self.val = val
                self.children = children
    """

    def postorder(self, root: "Node") -> list[int]:
        def traverse(node):
            # If the current node is None, return an empty list
            if not node:
                return []
            # Initialize an empty list to store the result
            result = []
            # Recursively traverse each child and extend the result list
            for child in node.children:
                result.extend(traverse(child))
            # Append the current node's value after traversing children
            result.append(node.val)
            return result
        
        # Start the traversal from the root
        return traverse(root)