# https://leetcode.com/problems/boats-to-save-people/


class Solution:
    """881. Boats to Save People

    You are given an array `people` where `people[i]` is the weight of the `ith` person,
    and an **infinite number of boats** where each boat can carry a maximum weight of
    `limit`. Each boat carries at most two people at the same time, provided the sum of
    the weight of those people is at most `limit`.

    Return *the minimum number of boats to carry every given person*.

    """

    def num_rescue_boats(self, people: list[int], limit: int) -> int: ...

    numRescueBoats = num_rescue_boats
