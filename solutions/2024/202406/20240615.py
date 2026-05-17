# https://leetcode.com/problems/ipo/
import heapq


class Solution:
    """502. IPO

    Suppose LeetCode will start its **IPO** soon. In order to sell a good price of its
    shares to Venture Capital, LeetCode would like to work on some projects to increase
    its capital before the **IPO**. Since it has limited resources, it can only finish
    at most `k` distinct projects before the **IPO**. Help LeetCode design the best way
    to maximize its total capital after finishing at most `k` distinct projects.

    You are given `n` projects where the `ith` project has a pure profit `profits[i]`
    and a minimum capital of `capital[i]` is needed to start it.

    Initially, you have `w` capital. When you finish a project, you will obtain its pure
    profit and the profit will be added to your total capital.

    Pick a list of **at most** `k` distinct projects from given projects to **maximize
    your final capital**, and return *the final maximized capital*.

    The answer is guaranteed to fit in a 32-bit signed integer.

    """

    def find_maximized_capital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        # Pair up profits and capital and sort them by the capital required
        projects = sorted(zip(capital, profits))

        max_profit_heap = []
        current_capital = w
        project_index = 0

        for _ in range(k):
            # Add all projects that can be started with the current capital to the max heap
            while (
                project_index < len(projects)
                and projects[project_index][0] <= current_capital
            ):
                # Use a negative profit to simulate max-heap in Python's min-heap
                heapq.heappush(max_profit_heap, -projects[project_index][1])
                project_index += 1

            # If there are no projects that can be started, break early
            if not max_profit_heap:
                break

            # Select the project with the maximum profit
            current_capital += -heapq.heappop(max_profit_heap)

        return current_capital

    findMaximizedCapital = find_maximized_capital
