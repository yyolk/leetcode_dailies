# https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution:
    """983. Minimum Cost For Tickets

    You have planned some train traveling one year in advance. The days of the year in
    which you will travel are given as an integer array `days`. Each day is an integer
    from `1` to `365`.

    Train tickets are sold in **three different ways**:

    * a **1-day** pass is sold for `costs[0]` dollars,

    * a **7-day** pass is sold for `costs[1]` dollars, and

    * a **30-day** pass is sold for `costs[2]` dollars.

    The passes allow that many days of consecutive travel.

    * For example, if we get a **7-day** pass on day `2`, then we can travel for `7`
    days: `2`, `3`, `4`, `5`, `6`, `7`, and `8`.

    Return *the minimum number of dollars you need to travel every day in the given list
    of days*."""

    def mincost_tickets(self, days: list[int], costs: list[int]) -> int:
        # Convert days to a set for O(1) lookup
        travel_days = set(days)
        last_day = days[-1]

        # Initialize dp array
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                # If we need to travel on this day, compute the cost for each pass option
                dp[day] = min(
                    # 1-day pass
                    dp[max(0, day - 1)] + costs[0],
                    # 7-day pass
                    dp[max(0, day - 7)] + costs[1],
                    # 30-day pass
                    dp[max(0, day - 30)] + costs[2],
                )

        return dp[last_day]

    mincostTickets = mincost_tickets
