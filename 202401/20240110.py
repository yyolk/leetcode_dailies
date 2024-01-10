# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
from collections import defaultdict, deque


class Solution:
    """2385. Amount of Time for Binary Tree to Be Infected

    You are given the `root` of a binary tree with **unique** values, and an integer
    `start`. At minute `0`, an **infection** starts from the node with value `start`.

    Each minute, a node becomes infected if:

    * The node is currently uninfected.

    * The node is adjacent to an infected node.

    Return *the number of minutes needed for the entire tree to be infected.*

    Definition for a binary tree node:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    """

    def amount_of_time(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            """Function to perform DFS and populate the graph with edges."""
            if node is None:
                return
            if node.left:
                # Add edge between current node and its left child
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                # Add edge between current node and its right child
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            # Recursively call DFS on left and right children
            dfs(node.left)
            dfs(node.right)

        # Initialize an empty graph as a defaultdict of lists
        graph = defaultdict(list)
        # Populate the graph using DFS
        dfs(root)

        # Initialize a set to track visited nodes and a queue for BFS
        visited = set()
        queue = deque([start])
        time = -1

        # Perform BFS
        while queue:
            time += 1
            # Process nodes at the current level
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                # Enqueue unvisited neighbors
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        # Return the total time taken for the entire tree to be infected
        return time

    amountOfTime = amount_of_time
