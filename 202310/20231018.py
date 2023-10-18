# https://leetcode.com/problems/parallel-courses-iii/


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
        ...

    minimumTime = minimum_time
