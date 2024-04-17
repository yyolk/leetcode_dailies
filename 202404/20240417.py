# https://leetcode.com/problems/smallest-string-starting-from-leaf/


class Solution:
    """988. Smallest String Starting From Leaf

    You are given the `root` of a binary tree where each node has a value in the range
    `[0, 25]` representing the letters `'a'` to `'z'`.

    Return *the **lexicographically smallest** string that starts at a leaf of this tree
    and ends at the root*.

    As a reminder, any shorter prefix of a string is **lexicographically smaller**.

    * For example, `"ab"` is lexicographically smaller than `"aba"`.

    A leaf of a node is a node that has no children.

    """

    def smallest_from_leaf(self, root: Optional[TreeNode]) -> str: ...

    smallestFromLeaf = smallest_from_leaf
