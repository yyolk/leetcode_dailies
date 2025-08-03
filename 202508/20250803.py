# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/


class Solution:
    """2106. Maximum Fruits Harvested After at Most K Steps

    Fruits are available at some positions on an infinite x-axis. You are given a 2D
    integer array `fruits` where `fruits[i] = [positioni, amounti]` depicts `amounti`
    fruits at the position `positioni`. `fruits` is already **sorted** by `positioni` in
    **ascending order**, and each `positioni` is **unique**.

    You are also given an integer `start_pos` and an integer `k`. Initially, you are at
    the position `start_pos`. From any position, you can either walk to the **left or
    right**. It takes **one step** to move **one unit** on the x-axis, and you can walk
    **at most** `k` steps in total. For every position you reach, you harvest all the
    fruits at that position, and the fruits will disappear from that position.

    Return *the **maximum total number** of fruits you can harvest*."""

    def max_total_fruits(
        self, fruits: list[list[int]], start_pos: int, k: int
    ) -> int: ...

    maxTotalFruits = max_total_fruits
