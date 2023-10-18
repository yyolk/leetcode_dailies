# https://leetcode.com/problems/parallel-courses-iii/
from collections import deque


class Solution:
    """2050. Parallel Courses III

    You are given an integer `n`, which indicates that there are `n` courses labeled
    from `1` to `n`. You are also given a 2D integer array `relations` where
    `relations[j] = [prevCoursej, nextCoursej]` denotes that course `prevCoursej` has to
    be completed **before** course `nextCoursej` (prerequisite relationship).
    Furthermore, you are given a **0-indexed** integer array `time` where `time[i]`
    denotes how many **months** it takes to complete the `(i+1)th` course.

    You must find the **minimum** number of months needed to complete all the courses
    following these rules:

    * You may start taking a course at **any time** if the prerequisites are met.

    * **Any number of courses** can be taken at the **same time**.

    Return *the **minimum** number of months needed to complete all the courses*.

    **Note:** The test cases are generated such that it is possible to complete every
    course (i.e., the graph is a directed acyclic graph).
    """

    def minimum_time(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """Finds the minimum number of months needed to complete all the courses.

        Proposed solution using topological sorting and dynamic programing.

        Args:
            n (int): The number of courses, each labeled from 1 to n.
            relations (List of List of int): A 2D integer array where each element is
                a direct dependency (prevCourse has to be completed before nextCourse).
            time (List of int): 0-indexed integer array where time[i] denotes how many
                months it takes to complete the (i+1)_th course.

        Returns:
            int: The minimum number of months needed to complete all the courses.
        """
        # Build the directed graph.
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for relation in relations:
            prev_course, next_course = relation
            graph[prev_course - 1].append(next_course - 1)
            in_degree[next_course - 1] += 1

        # Initialize the queue with courses having no prerequisites.
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize time and dp array.
        months = 0
        dp = time[:]

        # Perform topological sort.
        while queue:
            months += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                for next_course in graph[course]:
                    in_degree[next_course] -= 1
                    dp[next_course] = max(
                        dp[next_course], dp[course] + time[next_course]
                    )
                    if in_degree[next_course] == 0:
                        queue.append(next_course)

        # Return the minimum time needed.
        return max(dp)

    minimumTime = minimum_time
