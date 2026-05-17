# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/
from collections import deque


class Solution:
    """2071. Maximum Number of Tasks You Can Assign

    You have `n` tasks and `m` workers. Each task has a strength requirement stored in a
    **0-indexed** integer array `tasks`, with the `ith` task requiring `tasks[i]`
    strength to complete. The strength of each worker is stored in a **0-indexed**
    integer array `workers`, with the `jth` worker having `workers[j]` strength. Each
    worker can only be assigned to a **single** task and must have a strength **greater
    than or equal** to the task's strength requirement (i.e., `workers[j] >= tasks[i]`).

    Additionally, you have `pills` magical pills that will **increase a worker's
    strength** by `strength`. You can decide which workers receive the magical pills,
    however, you may only give each worker **at most one** magical pill.

    Given the **0-indexed** integer arrays `tasks` and `workers` and the integers
    `pills` and `strength`, return *the **maximum** number of tasks that can be
    completed.*"""

    def max_task_assign(
        self,
        tasks: list[int],
        workers: list[int],
        available_pills: int,
        pill_strength: int,
    ) -> int:
        # Sort the list of tasks in ascending order to handle easier tasks first
        tasks.sort()
        # Sort the list of workers in descending order to utilize stronger workers first
        workers.sort(reverse=True)

        # Define a helper function to determine if a given number of tasks can be assigned
        def can_assign_tasks(num_tasks: int) -> bool:
            # Initialize a pointer to track the current task index
            current_task_index = 0
            # Create a deque to store tasks that can potentially be assigned to the current worker
            assignable_tasks_queue = deque()
            # Copy the number of available pills for use in this check
            remaining_pills = available_pills
            # Iterate over workers from strongest to weakest, up to the number of tasks
            for worker_index in range(num_tasks - 1, -1, -1):
                # Add tasks to the queue that the current worker can handle with or without a pill
                while (
                    current_task_index < num_tasks
                    and tasks[current_task_index]
                    <= workers[worker_index] + pill_strength
                ):
                    assignable_tasks_queue.append(tasks[current_task_index])
                    current_task_index += 1

                # Check if there are no tasks available for assignment
                if len(assignable_tasks_queue) == 0:
                    return False
                # Check if the worker can complete the easiest task without using a pill
                if workers[worker_index] >= assignable_tasks_queue[0]:
                    # Remove the easiest task from the queue as it is assigned
                    assignable_tasks_queue.popleft()
                # Check if there are pills available to boost the worker's strength
                elif remaining_pills > 0:
                    # Remove the hardest task from the queue, using a pill
                    assignable_tasks_queue.pop()
                    remaining_pills -= 1
                else:
                    # If no tasks can be assigned and no pills are left, return False
                    return False
            # Return True if all tasks have been assigned successfully
            return True

        # Set the initial left bound for binary search
        left_bound = 0
        # Set the initial right bound as the minimum of tasks and workers length
        right_bound = min(len(tasks), len(workers))
        # Initialize a variable to store the maximum number of tasks that can be assigned
        max_assignable_tasks = -1
        # Perform binary search to find the maximum number of assignable tasks
        while left_bound <= right_bound:
            # Calculate the middle point for the binary search
            mid_point = (left_bound + right_bound) // 2
            # Check if the current number of tasks can be assigned
            if can_assign_tasks(mid_point):
                # Update the result with the current number of tasks
                max_assignable_tasks = mid_point
                # Move the left bound to search for a higher number
                left_bound = mid_point + 1
            else:
                # Move the right bound to search for a lower number
                right_bound = mid_point - 1
        # Return the maximum number of tasks that can be assigned
        return max_assignable_tasks

    maxTaskAssign = max_task_assign
