# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/


class Solution:
    """1203. Sort Items by Groups Respecting Dependencies

    There are `n` items each belonging to zero or one of `m` groups where `group[i]` is
    the group that the `i`-th item belongs to and it's equal to `-1` if the `i`-th item
    belongs to no group. The items and the groups are zero indexed. A group can have no
    item belonging to it.


    Return a sorted list of the items such that:

    * The items that belong to the same group are next to each other in the sorted list.

    * There are some relations between these items where `beforeItems[i]` is a list
    containing all the items that should come before the `i`-th item in the sorted
    array (to the left of the `i`-th item).


    Return any solution if there is more than one solution and return an **empty list**
    if there is no solution.
    """

    def sortItems(
        self, n: int, m: int, group: list[int], beforeItems: list[list[int]]
    ) -> list[int]:
        """Sort input items by groups respecting dependencies

        Proposed solution using a topological sort

        Args:
            n (int): number of items
            m (int): number of groups
            group (list of int): group mapping by index
            beforeItems (list of list of int): items to be inserted into the sort

        Returns:
            list of int: a solution where the input is sorted
        """

        # Helper function to perform topological sorting
        def topological_sort(graph, indegree, nodes):
            queue = [node for node in nodes if indegree[node] == 0]
            result = []
            while queue:
                node = queue.pop(0)
                result.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            return result

        # Step 1: Create a new group for items with group -1
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Step 2: Build directed graphs for both items and groups
        item_graph = [[] for _ in range(n)]
        group_graph = [[] for _ in range(m)]
        item_indegree = [0] * n
        group_indegree = [0] * m

        for i in range(n):
            for j in beforeItems[i]:
                item_graph[j].append(i)
                item_indegree[i] += 1
                if group[i] != group[j]:
                    group_graph[group[j]].append(group[i])
                    group_indegree[group[i]] += 1

        # Step 3: Topological sort within groups and among groups
        item_order = topological_sort(item_graph, item_indegree, range(n))
        group_order = topological_sort(group_graph, group_indegree, range(m))

        if len(item_order) != n or len(group_order) != m:
            return []

        # Step 4: Organize items within groups based on group_order
        group_items = defaultdict(list)
        for item in item_order:
            group_items[group[item]].append(item)

        result = []
        for group_id in group_order:
            result.extend(group_items[group_id])

        return result
