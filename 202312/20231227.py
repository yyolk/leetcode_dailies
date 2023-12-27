# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution:
    """1578. Minimum Time to Make Rope Colorful

    Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string
    `colors` where `colors[i]` is the color of the `ith` balloon.

    Alice wants the rope to be **colorful**. She does not want **two consecutive
    balloons** to be of the same color, so she asks Bob for help. Bob can remove some
    balloons from the rope to make it **colorful**. You are given a **0-indexed**
    integer array `needed_time` where `needed_time[i]` is the time (in seconds) that Bob
    needs to remove the `ith` balloon from the rope.

    Return *the **minimum time** Bob needs to make the rope **colorful***.
    """

    def min_cost(self, colors: str, needed_time: list[int]) -> int:
        ...

    minCost = min_cost
