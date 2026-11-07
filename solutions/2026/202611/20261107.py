# https://leetcode.com/problems/process-tasks-using-servers/


class Solution:
    """1882. Process Tasks Using Servers

    You are given two **0-indexed** integer arrays `servers` and `tasks` of lengths
    `n`\u200b\u200b\u200b\u200b\u200b\u200b and `m`\u200b\u200b\u200b\u200b\u200b\u200b respectively. `servers[i]` is the **weight** of the
    `i\u200b\u200b\u200b\u200b\u200b\u200bth`\u200b\u200b\u200b\u200b server, and `tasks[j]` is the **time needed** to process the
    `j\u200b\u200b\u200b\u200b\u200b\u200bth`\u200b\u200b\u200b\u200b task **in seconds**.

    Tasks are assigned to the servers using a **task queue**. Initially, all servers are
    free, and the queue is **empty**.

    At second `j`, the `jth` task is **inserted** into the queue (starting with the
    `0th` task being inserted at second `0`). As long as there are free servers and the
    queue is not empty, the task in the front of the queue will be assigned to a free
    server with the **smallest weight**, and in case of a tie, it is assigned to a free
    server with the **smallest index**.

    If there are no free servers and the queue is not empty, we wait until a server
    becomes free and immediately assign the next task. If multiple servers become free
    at the same time, then multiple tasks from the queue will be assigned **in order of
    insertion** following the weight and index priorities above.

    A server that is assigned task `j` at second `t` will be free again at second `t +
    tasks[j]`.

    Build an array `ans`\u200b\u200b\u200b\u200b of length `m`, where `ans[j]` is the **index** of the
    server the `j\u200b\u200b\u200b\u200b\u200b\u200bth` task will be assigned to.

    Return *the array* `ans`\u200b\u200b\u200b\u200b.

    Constraints:

    * `servers.length == n`

    * `tasks.length == m`

    * `1 <= n, m <= 2 * 105`

    * `1 <= servers[i], tasks[j] <= 2 * 105`"""

    def assign_tasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        """...

        Proposed solution ...

        Args:
            servers (list of int): ...
            tasks (list of int): ...

        Returns:
            list of int: ..."""
        ...

    assignTasks = assign_tasks
