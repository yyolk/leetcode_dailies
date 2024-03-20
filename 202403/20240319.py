# https://leetcode.com/problems/task-scheduler/
from collections import Counter


class Solution:
    """621. Task Scheduler

    You are given an array of CPU `tasks`, each represented by letters A to Z, and a
    cooling time, `n`. Each cycle or interval allows the completion of one task. Tasks
    can be completed in any order, but there's a constraint: **identical** tasks must be
    separated by at least `n` intervals due to cooling time.

    Return the *minimum number of intervals* required to complete all tasks.

    """

    def least_interval(self, tasks: list[str], n: int) -> int:
        # Count the occurrences of each task
        task_counts = Counter(tasks)

        # Find the maximum count of any task
        max_count = max(task_counts.values())

        # Count the number of tasks with the maximum count
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)

        # Calculate the intervals needed based on the cooling time constraint
        intervals_needed = (max_count - 1) * (n + 1) + max_count_tasks

        # Return the maximum of either the total number of tasks or the calculated intervals needed
        return max(len(tasks), intervals_needed)

    leastInterval = least_interval

