# https://leetcode.com/problems/course-schedule-iv/
from collections import deque


class Solution:
    """1462. Course Schedule IV

    There are a total of `num_courses` courses you have to take, labeled from `0` to
    `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] =
    [ai, bi]` indicates that you **must** take course `ai` first if you want to take
    course `bi`.

    * For example, the pair `[0, 1]` indicates that you have to take course `0` before
    you can take course `1`.

    Prerequisites can also be **indirect**. If course `a` is a prerequisite of course
    `b`, and course `b` is a prerequisite of course `c`, then course `a` is a
    prerequisite of course `c`.

    You are also given an array `queries` where `queries[j] = [uj, vj]`. For the `jth`
    query, you should answer whether course `uj` is a prerequisite of course `vj` or
    not.

    Return *a boolean array* `answer`*, where* `answer[j]` *is the answer to the* `jth`
    *query.*"""

    def check_if_prerequisite(
        self, num_courses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        # Build adjacency list
        adj = [[] for _ in range(num_courses)]
        for a, b in prerequisites:
            adj[a].append(b)

        # Precompute reachable sets using BFS for each node
        reachable = [set() for _ in range(num_courses)]
        for u in range(num_courses):
            queue = deque([u])
            visited = set()
            visited.add(u)
            while queue:
                current = queue.popleft()
                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            reachable[u] = visited

        # Process each query
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(False)
            else:
                answer.append(v in reachable[u])

        return answer

    checkIfPrerequisite = check_if_prerequisite
