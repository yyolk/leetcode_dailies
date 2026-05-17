# https://leetcode.com/problems/most-profit-assigning-work/


class Solution:
    """826. Most Profit Assigning Work

    You have `n` jobs and `m` workers. You are given three arrays: `difficulty`,
    `profit`, and `worker` where:

    * `difficulty[i]` and `profit[i]` are the difficulty and the profit of the `ith`
    job, and

    * `worker[j]` is the ability of `jth` worker (i.e., the `jth` worker can only
    complete a job with difficulty at most `worker[j]`).

    Every worker can be assigned **at most one job**, but one job can be **completed
    multiple times**.

    * For example, if three workers attempt the same job that pays `$1`, then the total
    profit will be `$3`. If a worker cannot complete any job, their profit is `$0`.

    Return the maximum profit we can achieve after assigning the workers to the jobs.

    """

    def max_profit_assignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        # Step 1: Combine difficulty and profit into a list of tuples and sort by difficulty
        jobs = sorted(zip(difficulty, profit))

        # Step 2: Sort the workers by their ability
        worker.sort()

        max_profit = 0  # To track the maximum profit for a worker
        total_profit = 0  # To accumulate the total profit
        job_index = 0  # To iterate through the jobs

        # Step 3: Iterate through each worker
        for w in worker:
            # While there are jobs within the current worker's ability, update max_profit
            while job_index < len(jobs) and jobs[job_index][0] <= w:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the maximum profit for this worker to the total profit
            total_profit += max_profit

        return total_profit

    maxProfitAssignment = max_profit_assignment
