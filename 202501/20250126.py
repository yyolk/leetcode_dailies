# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/
from collections import defaultdict


class Solution:
    """2127. Maximum Employees to Be Invited to a Meeting

    A company is organizing a meeting and has a list of `n` employees, waiting to be
    invited. They have arranged for a large **circular** table, capable of seating **any
    number** of employees.

    The employees are numbered from `0` to `n - 1`. Each employee has a **favorite**
    person and they will attend the meeting **only if** they can sit next to their
    favorite person at the table. The favorite person of an employee is **not**
    themself.

    Given a **0-indexed** integer array `favorite`, where `favorite[i]` denotes the
    favorite person of the `ith` employee, return *the **maximum number of employees**
    that can be invited to the meeting*."""

    def maximum_invitations(self, favorite: list[int]) -> int:
        # Create adjacency list for the directed graph
        employee_to_favorite = defaultdict(list)
        # Create the transpose of the graph for Kosaraju's algorithm
        favorite_to_employee = defaultdict(list)

        # Populate the adjacency list and its transpose
        for employee_index in range(len(favorite)):
            employee_to_favorite[employee_index].append(favorite[employee_index])
            favorite_to_employee[favorite[employee_index]].append(employee_index)

        # Stack for DFS in first pass of Kosaraju's algorithm
        dfs_stack = []
        # Track visited nodes during first DFS
        first_visit = [False] * len(favorite)

        def dfs_first_pass(node):
            # Mark node as visited in first DFS
            first_visit[node] = True
            # Visit all adjacent nodes not yet visited
            for neighbor in employee_to_favorite[node]:
                if not first_visit[neighbor]:
                    dfs_first_pass(neighbor)
            # Add node to stack after visiting all its neighbors
            dfs_stack.append(node)

        # Perform first DFS to fill stack for second DFS
        for employee_index in range(len(favorite)):
            if not first_visit[employee_index]:
                dfs_first_pass(employee_index)

        # List to hold strongly connected components (SCCs)
        strongly_connected_components = []
        # Current SCC being built
        current_scc = set()
        # Reset visited array for the second pass of Kosaraju's algorithm
        second_visit = [False] * len(favorite)

        def dfs_second_pass(node):
            # Mark node as visited in second DFS
            second_visit[node] = True
            # Add node to the current SCC
            current_scc.add(node)
            # Visit all adjacent nodes in the transposed graph
            for neighbor in favorite_to_employee[node]:
                if not second_visit[neighbor]:
                    dfs_second_pass(neighbor)

        # Process nodes from stack to find SCCs
        while dfs_stack:
            top_node = dfs_stack.pop()
            if not second_visit[top_node]:
                current_scc = set()
                dfs_second_pass(top_node)
                strongly_connected_components.append(current_scc)

        # Find maximum size of SCCs, ignoring two-node cycles for now
        max_scc_size = max(
            [len(scc) if len(scc) != 2 else -1 for scc in strongly_connected_components]
        )

        # Function to find the longest path from 'a' avoiding 'b'
        def find_longest_path(a, b):
            length = 0
            for next_node in favorite_to_employee[a]:
                if next_node != b:
                    length = max(length, 1 + find_longest_path(next_node, b))
            return length

        # Count employees for two-node cycles with additional paths
        count_two_node_cycles = 0
        for scc in strongly_connected_components:
            if len(scc) == 2:
                employee1, employee2 = list(scc)
                count_two_node_cycles += (
                    2
                    + find_longest_path(employee1, employee2)
                    + find_longest_path(employee2, employee1)
                )

        # Return the maximum of direct SCC size or combined two-node cycles
        return max(max_scc_size, count_two_node_cycles)

    maximumInvitations = maximum_invitations
