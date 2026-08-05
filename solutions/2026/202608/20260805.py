# https://leetcode.com/problems/remove-methods-from-project/

class Solution:
    """3310. Remove Methods From Project

    You are maintaining a project that has n methods numbered from 0 to n - 1.
    You are given two integers n and k, and a 2D integer array invocations, where
    invocations[i] = [ai, bi] indicates that method ai invokes method bi.

    There is a known bug in method k. Method k, along with any method invoked by
    it, either directly or indirectly, are considered suspicious and we aim to
    remove them.

    A group of methods can only be removed if no method outside the group invokes
    any methods within it.

    Return an array containing all the remaining methods after removing all the
    suspicious methods. You may return the answer in any order. If it is not
    possible to remove all the suspicious methods, none should be removed.
    """
    def remaining_methods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        # Track which methods are reachable from the buggy method k
        suspicious = [False] * n
        # Directed adjacency list: invoker -> list of methods it calls
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        # Iterative DFS to mark all methods reachable from k as suspicious
        stack = [k]
        suspicious[k] = True
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    stack.append(nxt)
        # If any non-suspicious method calls a suspicious one, removal is illegal
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))
        # Otherwise return every method that is not suspicious
        return [i for i in range(n) if not suspicious[i]]

    remainingMethods = remaining_methods
