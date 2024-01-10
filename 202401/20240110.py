# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/


class Solution:
    """2385. Amount of Time for Binary Tree to Be Infected

    You are given the `root` of a binary tree with **unique** values, and an integer
    `start`. At minute `0`, an **infection** starts from the node with value `start`.

    Each minute, a node becomes infected if:

    * The node is currently uninfected.

    * The node is adjacent to an infected node.

    Return *the number of minutes needed for the entire tree to be infected.*
    """

    def amount_of_time(self, root: Optional[TreeNode], start: int) -> int:
        ...

    amountOfTime = amount_of_time
