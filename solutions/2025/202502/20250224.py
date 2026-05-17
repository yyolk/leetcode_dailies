# https://leetcode.com/problems/most-profitable-path-in-a-tree/


class Solution:
    """2467. Most Profitable Path in a Tree

    There is an undirected tree with `n` nodes labeled from `0` to `n - 1`, rooted at
    node `0`. You are given a 2D integer array `edges` of length `n - 1` where `edges[i]
    = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

    At every node `i`, there is a gate. You are also given an array of even integers
    `amount`, where `amount[i]` represents:

    * the price needed to open the gate at node `i`, if `amount[i]` is negative, or,

    * the cash reward obtained on opening the gate at node `i`, otherwise.

    The game goes on as follows:

    * Initially, Alice is at node `0` and Bob is at node `bob`.

    * At every second, Alice and Bob **each** move to an adjacent node. Alice moves
    towards some **leaf node**, while Bob moves towards node `0`.

    * For **every** node along their path, Alice and Bob either spend money to open the
    gate at that node, or accept the reward. Note that:

      + If the gate is **already open**, no price will be required, nor will there be
    any cash reward.

      + If Alice and Bob reach the node **simultaneously**, they share the price/reward
    for opening the gate there. In other words, if the price to open the gate is `c`,
    then both Alice and Bob pay `c / 2` each. Similarly, if the reward at the gate is
    `c`, both of them receive `c / 2` each.

    * If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node
    `0`, he stops moving. Note that these events are **independent** of each other.

    Return *the **maximum** net income Alice can have if she travels towards the optimal
    leaf node.*"""

    def most_profitable_path(
        self, edges: list[list[int]], bob: int, amount: list[int]
    ) -> int:
        # Build adjacency list representation of the tree
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Track Bob's path to node 0
        bob_path = []

        def find_bob_path(node: int, parent: int) -> bool:
            if node == bob:
                bob_path.append(node)
                return True

            for next_node in graph[node]:
                if next_node != parent:
                    if find_bob_path(next_node, node):
                        bob_path.append(node)
                        return True
            return False

        find_bob_path(0, -1)

        # Calculate time when Bob reaches each node on his path
        bob_time = {}
        for i, node in enumerate(bob_path):
            bob_time[node] = i

        # DFS to find Alice's most profitable path
        def dfs(node: int, parent: int, time: int, income: int) -> int:
            # Calculate current node's contribution
            curr_amount = amount[node]
            if node in bob_time and bob_time[node] == time:
                # Alice and Bob meet simultaneously, split the amount
                curr_amount //= 2
            elif node in bob_time and bob_time[node] < time:
                # Bob already passed, no amount to collect/spend
                curr_amount = 0

            # If leaf node (only one neighbor which is parent)
            if len(graph[node]) == 1 and parent != -1:
                return income + curr_amount

            # Explore all children
            max_income = float("-inf")
            for next_node in graph[node]:
                if next_node != parent:
                    max_income = max(
                        max_income, dfs(next_node, node, time + 1, income + curr_amount)
                    )
            return max_income

        return dfs(0, -1, 0, 0)

    mostProfitablePath = most_profitable_path
