# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution:
    """1578. Minimum Time to Make Rope Colorful

    Alice has n balloons arranged on a rope. You are given a 0-indexed string
    colors where colors[i] is the color of the ith balloon.

    Alice wants the rope to be colorful. She does not want two consecutive
    balloons to be of the same color, so she asks Bob for help. Bob can remove
    some balloons from the rope to make it colorful. You are given a 0-indexed
    integer array neededTime where neededTime[i] is the time (in seconds) that
    Bob needs to remove the ith balloon from the rope.

    Return the minimum time Bob needs to make the rope colorful.
    """
    def min_cost(self, colors: str, needed_time: list[int]) -> int:
        # Initialize total cost to 0
        total_cost = 0
        n = len(colors)
        i = 0
        # Traverse the string to find groups of consecutive same colors
        while i < n:
            j = i
            # Extend j to the end of the current group
            while j < n and colors[j] == colors[i]:
                j += 1
            # If group size > 1, calculate cost: sum of times minus max time
            if j - i > 1:
                group_times = needed_time[i:j]
                total_cost += sum(group_times) - max(group_times)
            # Move to the next group
            i = j
        return total_cost

    minCost = min_cost