# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
import heapq


class Solution:
    """857. Minimum Cost to Hire K Workers

    There are `n` workers. You are given two integer arrays `quality` and `wage` where
    `quality[i]` is the quality of the `ith` worker and `wage[i]` is the minimum wage
    expectation for the `ith` worker.

    We want to hire exactly `k` workers to form a **paid group**. To hire a group of `k`
    workers, we must pay them according to the following rules:

    1. Every worker in the paid group must be paid at least their minimum wage
    expectation.

    2. In the group, each worker's pay must be directly proportional to their quality.
    This means if a worker’s quality is double that of another worker in the group, then
    they must be paid twice as much as the other worker.

    Given the integer `k`, return *the least amount of money needed to form a paid group
    satisfying the above conditions*. Answers within `10-5` of the actual answer will be
    accepted.

    """

    def mincost_to_hire_workers(
        self, quality: list[int], wage: list[int], k: int
    ) -> float:
        # Calculate the wage-to-quality ratio for each worker
        n = len(quality)
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])

        min_cost = float("inf")
        total_quality = 0
        heap = []

        for ratio, q in workers:
            total_quality += q
            # Max heap for quality
            heapq.heappush(heap, -q)

            if len(heap) > k:
                # Remove the worker with max quality
                total_quality += heapq.heappop(heap)

            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost

    mincostToHireWorkers = mincost_to_hire_workers
