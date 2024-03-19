# https://leetcode.com/problems/task-scheduler/


class Solution:
    """621. Task Scheduler

    You are given an array of CPU `tasks`, each represented by letters A to Z, and a
    cooling time, `n`. Each cycle or interval allows the completion of one task. Tasks
    can be completed in any order, but there's a constraint: **identical** tasks must be
    separated by at least `n` intervals due to cooling time.

    \u200bReturn the *minimum number of intervals* required to complete all tasks.

    """

    def least_interval(self, tasks: list[str], n: int) -> int: ...

    leastInterval = least_interval
