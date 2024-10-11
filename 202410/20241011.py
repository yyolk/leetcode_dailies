# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/


class Solution:
    """1942. The Number of the Smallest Unoccupied Chair

    There is a party where `n` friends numbered from `0` to `n - 1` are attending. There
    is an **infinite** number of chairs in this party that are numbered from `0` to
    `infinity`. When a friend arrives at the party, they sit on the unoccupied chair
    with the **smallest number**.

    * For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they
    will sit on chair number `2`.

    When a friend leaves the party, their chair becomes unoccupied at the moment they
    leave. If another friend arrives at that same moment, they can sit in that chair.

    You are given a **0\\-indexed** 2D integer array `times` where `times[i] = [arrivali,
    leavingi]`, indicating the arrival and leaving times of the `ith` friend
    respectively, and an integer `target_friend`. All arrival times are **distinct**.

    Return *the **chair number** that the friend numbered* `target_friend` *will sit
    on*.

    """

    def smallest_chair(self, times: list[list[int]], target_friend: int) -> int: ...

    smallestChair = smallest_chair
