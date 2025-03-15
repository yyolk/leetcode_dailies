# https://leetcode.com/problems/house-robber-iv/


class Solution:
    """2560. House Robber IV

    There are several consecutive houses along a street, each of which has some money
    inside. There is also a robber, who wants to steal money from the homes, but he
    **refuses to steal from adjacent homes**.

    The **capability** of the robber is the maximum amount of money he steals from one
    house of all the houses he robbed.

    You are given an integer array `nums` representing how much money is stashed in each
    house. More formally, the `ith` house from the left has `nums[i]` dollars.

    You are also given an integer `k`, representing the **minimum** number of houses the
    robber will steal from. It is always possible to steal at least `k` houses.

    Return *the **minimum** capability of the robber out of all the possible ways to
    steal at least* `k` *houses*."""

    def min_capability(self, nums: list[int], k: int) -> int: ...

    minCapability = min_capability
