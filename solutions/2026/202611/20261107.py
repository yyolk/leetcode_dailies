# https://leetcode.com/problems/process-tasks-using-servers/
import heapq


class Solution:
    """1882. Process Tasks Using Servers

    You are given two 0-indexed integer arrays servers and tasks of lengths
    n and m respectively. servers[i] is the weight of the i-th server, and
    tasks[j] is the time needed to process the j-th task in seconds.

    Tasks are assigned to the servers using a task queue. Initially, all
    servers are free, and the queue is empty.

    At second j, the j-th task is inserted into the queue (starting with the
    0-th task being inserted at second 0). As long as there are free servers
    and the queue is not empty, the task in the front of the queue will be
    assigned to a free server with the smallest weight, and in case of a tie,
    it is assigned to a free server with the smallest index.

    If there are no free servers and the queue is not empty, we wait until a
    server becomes free and immediately assign the next task. If multiple
    servers become free at the same time, then multiple tasks from the queue
    will be assigned in order of insertion following the weight and index
    priorities above.

    A server that is assigned task j at second t will be free again at second
    t + tasks[j].

    Build an array ans of length m, where ans[j] is the index of the server
    the j-th task will be assigned to.

    Return the array ans.

    Constraints:

    * servers.length == n

    * tasks.length == m

    * 1 <= n, m <= 2 * 10^5

    * 1 <= servers[i], tasks[j] <= 2 * 10^5
    """

    def assign_tasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # idle: (weight, index) — free servers, min-heap by weight then index
        idle = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(idle)

        # busy: (free_time, weight, index) — occupied servers by completion time
        busy: list[tuple[int, int, int]] = []

        ans: list[int] = []
        time = 0

        for task_index, duration in enumerate(tasks):
            # Current time is at least the task arrival time.
            time = max(time, task_index)

            # Release all servers that finish by the current time.
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(idle, (weight, index))

            # If no idle server, jump to the earliest completion time.
            if not idle:
                free_time, weight, index = heapq.heappop(busy)
                time = free_time
                heapq.heappush(idle, (weight, index))
                # Release any other servers that finish at the same moment.
                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(idle, (weight, index))

            # Assign the free server with smallest weight (then index).
            weight, index = heapq.heappop(idle)
            ans.append(index)
            heapq.heappush(busy, (time + duration, weight, index))

        return ans

    assignTasks = assign_tasks
