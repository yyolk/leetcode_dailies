import heapq

class TaskManager:
    """3678. Design Task Manager

    There is a task management system that allows users to manage their tasks, each
    associated with a priority. The system should efficiently handle adding, modifying,
    executing, and removing tasks.

    Implement the `TaskManager` class:

    * `TaskManager(vector<vector<int>>& tasks)` initializes the task manager with a list
    of user-task-priority triples. Each element in the input list is of the form
    `[userId, taskId, priority]`, which adds a task to the specified user with the given
    priority.

    * `void add(int userId, int taskId, int priority)` adds a task with the specified
    `taskId` and `priority` to the user with `userId`. It is **guaranteed** that
    `taskId` does not *exist* in the system.

    * `void edit(int taskId, int newPriority)` updates the priority of the existing
    `taskId` to `newPriority`. It is **guaranteed** that `taskId` *exists* in the
    system.

    * `void rmv(int taskId)` removes the task identified by `taskId` from the system. It
    is **guaranteed** that `taskId` *exists* in the system.

    * `int execTop()` executes the task with the **highest** priority across all users.
    If there are multiple tasks with the same **highest** priority, execute the one with
    the highest `taskId`. After executing, the`taskId`is **removed** from the system.
    Return the `userId` associated with the executed task. If no tasks are available,
    return -1.

    **Note** that a user may be assigned multiple tasks."""

    def __init__(self, tasks: list[list[int]]):
        # Dictionary to map taskId to (userId, priority)
        self.task_to_info = {}
        # Min-heap simulating max-heap for (priority, taskId); use negatives for max
        self.heap = []
        # Add initial tasks to info and heap
        for user_id, task_id, prio in tasks:
            self.task_to_info[task_id] = (user_id, prio)
            heapq.heappush(self.heap, (-prio, -task_id, task_id))

    def add(self, userId: int, task_id: int, priority: int) -> None:
        # Store task info
        self.task_to_info[task_id] = (userId, priority)
        # Push to heap: (-priority, -task_id, task_id) for max priority then max task_id
        heapq.heappush(self.heap, (-priority, -task_id, task_id))

    def edit(self, taskId: int, new_priority: int) -> None:
        # Retrieve existing userId
        user_id, _ = self.task_to_info[taskId]
        # Update priority in info
        self.task_to_info[taskId] = (user_id, new_priority)
        # Push updated entry to heap; old entry will be discarded if popped later
        heapq.heappush(self.heap, (-new_priority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        # Remove from info dict; heap entries will be ignored if popped
        del self.task_to_info[taskId]

    def execTop(self) -> int:
        # Pop heap until valid top task found
        while self.heap:
            neg_prio, neg_tid, tid = heapq.heappop(self.heap)
            prio = -neg_prio
            # Validate: task exists and priority matches pushed value
            if tid in self.task_to_info and self.task_to_info[tid][1] == prio:
                # Extract userId and remove task
                user_id, _ = self.task_to_info[tid]
                del self.task_to_info[tid]
                return user_id
        # No valid tasks
        return -1